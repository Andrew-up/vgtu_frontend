import base64
import datetime
import sys
import time

import cv2
from PySide6.QtCore import Slot
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtWidgets import QWidget, QApplication, QFileDialog, QPushButton, QDialog, QVBoxLayout, QButtonGroup, \
    QRadioButton

from definitions import DATASET_PATH, MODEL_H5_PATH

from model.result_scan import ResultScan
from model.history_patient import HistoryPatient
from model.history_neural_network import HistoryNeuralNetwork
from service.unetModelService import LoadingModelAndPredict
from service.PatientService import PatientServiceFront
from view.py.wound_healing_widget import Ui_Form
from view.user.drawing_counter import DrawingCounter
from service.imageService import ImageConverter, image_to_base64
from model.patient_model import Patient
from utils.message_box import message_error_show, message_info_show


class WoundHealingPatient(QWidget):

    def __init__(self, patient: Patient = None, parent=None):
        super(WoundHealingPatient, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.patient_id = 0
        self.hide_widget()
        self.ui.wound_healing_start_scan.clicked.connect(self.start_scan)
        self.ui.radio_scan_to_photo_catalog.clicked.connect(self.on_radio_scan_from_catalog)
        self.ui.radio_scan_to_cam.clicked.connect(self.on_radio_scan_to_cam)
        self.ui.button_select_ptoho_from_catalog.setVisible(False)

        # ------- Отдельный поток и связка сигналов
        self.load_model_and_predict = LoadingModelAndPredict(MODEL_H5_PATH)
        self.load_model_and_predict.setObjectName('LOAD_MODEL_THREAD')
        self.load_model_and_predict.loading_model_end.connect(self.on_load_model_end_signal)
        self.load_model_and_predict.image_original.connect(self.setImage_Original)
        self.load_model_and_predict.video_stream_image.connect(self.playVideoStream)
        self.load_model_and_predict.predict_image_result.connect(self.setImage_Predict)
        self.load_model_and_predict.result_scan.connect(self.result_scan_init)
        self.load_model_and_predict.set_categorical_predict(self.get_predict_categorical())
        print(self.load_model_and_predict.categorical_predict)
        # -------

        # Связка кнопок Результат корректен ?
        self.ui.wound_healing_button_result_yes.clicked.connect(self.on_result_is_ok)
        self.ui.wound_healing_button_result_no.clicked.connect(self.on_result_is_not_ok)
        # -------
        self.ui.button_select_ptoho_from_catalog.clicked.connect(self.open_file_from_catalog)
        self.image_original = None
        self.history_n_n: HistoryNeuralNetwork = HistoryNeuralNetwork()
        if patient is not None:
            self.patient_id = patient.id_patient
            self.ui.wound_healing_fullname_client.setText(patient.full_name)
            self.ui.wound_healing_diagnosis_client.setText(patient.dianosis)


    def get_predict_categorical(self):
        return PatientServiceFront(1).get_all_categorical()

    def on_result_is_ok(self):
        history = HistoryPatient()
        history.date = str(datetime.datetime.now())
        history.comment = 'тест'
        history.patient_id = self.patient_id
        # history_nn = HistoryNeuralNetwork()
        # history_nn.result_predict_id = 1
        # history_nn.photo_original = '12312312'
        # history_nn.photo_predict = 'ssssss'
        # history.comment = 'comment-test'
        # history.date = 'date-test'
        history.history_neutral_network = self.history_n_n.__dict__

        # history.patient_id = 1
        s = PatientServiceFront(1)
        status_code, text = s.addHistoryPatient(history)
        if status_code != 200:
            message_error_show(self, text)
        else:
            message_info_show(self, text)

        # print(self.image_original)
        print('результат ок, надо сохранить')
        self.block_result_scan_widget()
        self.ui.widget.setVisible(True)

    def on_result_is_not_ok(self):
        dlg = DrawingCounter(self.image_original)
        dlg.image_result_edit_doctor.connect(self.setImage_Predict_edit)
        dlg.history_n_n.connect(self.init_history_nn_edit)
        print('результат не правильный, надо редактировать')
        dlg.exec()

    def block_result_scan_widget(self):
        print('block')
        self.ui.wound_healing_button_result_yes.setEnabled(False)
        self.ui.wound_healing_button_result_no.setEnabled(False)

    def unblock_result_scan_widget(self):
        print('unblock')
        self.ui.wound_healing_button_result_yes.setEnabled(True)
        self.ui.wound_healing_button_result_no.setEnabled(True)

    @Slot(HistoryNeuralNetwork)
    def init_history_nn_edit(self, h: HistoryNeuralNetwork):
        self.ui.wound_healing_area_wound.setText(f"Площадь: {h.area_wound}")
        self.ui.wound_healing_type_wound.setText(f"Тип раны: {h.result_predict.name_category_ru}")
        # self.history_n_n.polygon_mask = h.polygon_mask
        base64_polygon = base64.b64encode(str(h.polygon_mask).encode())
        self.history_n_n.polygon_mask = str(base64_polygon)
        self.history_n_n.result_predict_id = h.result_predict_id
        print(h.result_predict_id)
        # print(base64_polygon)
        # print(h.polygon_mask)
        # print(h.area_wound)

    def returnCameraIndexes(self):
        # checks the first 3 indexes.
        index = 0
        arr = []
        i = 3
        while i > 0:
            cap = cv2.VideoCapture(index, cv2.CAP_DSHOW)
            for jjjj in range(10):
                cap.read()
            success, img = cap.read()
            print(success)
            if cap.read()[0]:
                arr.append(index)
                print(index)
            # print(cap.read()[0])
            cap.release()
            cv2.destroyAllWindows()
            index += 1
            # print(i)
            i -= 1
        return arr

    @Slot(ResultScan)
    def result_scan_init(self, res: list[ResultScan]):
        self.ui.wound_healing_type_wound.setText('Тип раны: <br>')
        self.ui.wound_healing_area_wound.setText('Площадь: <br>')
        self.ui.label_9.setText(f'<font style="color:rgb(255, 0, 0);"> КОНТУР РАНЫ НЕ ОПРЕДЕЛЕН </font>')
        for i in res:
            self.ui.label_9.setText(f'<font style="color:rgb(0, 255, 0);"> КОНТУР РАНЫ ОПРЕДЕЛЕН </font>')
            # print(i.type_wound)
            # print('========================================')
            # print(i.polygon_wound)
            self.history_n_n.polygon_mask = i.polygon_wound
            self.history_n_n.result_predict_id = i.result_predict_id
            # print(i.color)
            self.ui.wound_healing_type_wound.setText(self.ui.wound_healing_type_wound.text() +
                                                     f'<font style="color:rgb{i.color};">{i.type_wound}</font>, ')

            self.ui.wound_healing_area_wound.setText(self.ui.wound_healing_area_wound.text() +
                                                     f'<font style="color:rgb{i.color};">{i.type_wound}</font>: {i.area_wound}, <br>')
            # self.ui.wound_healing_area_wound.setText(f'Площадь: {str(i.area_wound)}')

    def on_radio_scan_from_catalog(self):
        self.load_model_and_predict.play_video = False
        self.load_model_and_predict.scan_from_cam = False
        if self.ui.radio_scan_to_photo_catalog.isChecked():
            self.ui.button_select_ptoho_from_catalog.setVisible(True)
            # self.load_model_and_predict.scan_from_cam = False
            self.ui.wound_healing_start_scan.setEnabled(False)

    def check_cam_in_group(self, radio_group: QButtonGroup(), array_index_cam):
        a = 0
        for i in radio_group.buttons():
            if i.isChecked():
                self.ui.file_name_select_folder.setText('Выбрана камера: ' + str(array_index_cam[a]))
                self.load_model_and_predict.number_cam = array_index_cam[a]
                self.load_model_and_predict.number_cam = a
                return 0
            a += 1

    def on_radio_scan_to_cam(self):
        if self.load_model_and_predict.number_cam == -1:
            index_cam_arr = self.returnCameraIndexes()
            msg = QDialog()
            layout = QVBoxLayout()
            group = QButtonGroup()
            for i in range(len(index_cam_arr)):
                radio = QRadioButton()
                radio.setText('Камера: ' + str(i))
                layout.addWidget(radio)
                group.addButton(radio)
            button_ok = QPushButton()
            button_cancel = QPushButton()
            button_ok.setText("OK")
            button_ok.clicked.connect(lambda: self.check_cam_in_group(group, index_cam_arr))
            button_ok.clicked.connect(msg.close)
            button_cancel.clicked.connect(msg.close)
            button_cancel.setText("Отмена")
            layout.addWidget(button_ok)
            layout.addWidget(button_cancel)
            msg.setLayout(layout)
            msg.exec()
            # self.load_model_and_predict.start()
        # else:
        #     print('else')
        #     self.load_model_and_predict.play_video = True
        #     self.load_model_and_predict.start()

        if self.ui.radio_scan_to_cam.isChecked():
            self.load_model_and_predict.image_path = None
            self.ui.button_select_ptoho_from_catalog.setVisible(False)
            self.load_model_and_predict.scan_from_cam = True
            self.ui.wound_healing_start_scan.setEnabled(True)

    def hide_widget(self):
        # self.ui.wound_healing_widget.setVisible(False)
        self.ui.wound_healing_loading_label.setVisible(False)
        self.ui.wound_healing_start_scan.setEnabled(False)
        self.ui.widget.setVisible(False)
        self.ui.widget_2.setVisible(False)
        self.ui.label_12.setVisible(False)
        self.ui.wound_healing_STOP_robot.setVisible(False)
        self.ui.wound_healing_status_end_process.setVisible(False)

    def open_file_from_catalog(self):
        timing = time.time()
        fileName = QFileDialog.getOpenFileName(self, "Open Image", DATASET_PATH,
                                               "Image Files (*.png *.jpg, *.jpeg, *.tiff, *.*)")
        self.ui.file_name_select_folder.setText(fileName[0])
        if fileName[0] != '':
            self.load_model_and_predict.image_path = fileName[0]
            self.ui.wound_healing_start_scan.setEnabled(True)
        print(time.time() - timing)

    @Slot(str)
    def on_load_model_end_signal(self, time_load_model):
        self.ui.wound_healing_loading_label.setText(f'Модель была загружена за {time_load_model} секунды \n '
                                                    f'Идет распознавание болезни \n'
                                                    f'подождите....')
        print('модель загружена')

    @Slot(QImage)
    def playVideoStream(self, image):
        self.image_original = QPixmap.fromImage(image)
        self.ui.wound_healing_image.setPixmap(QPixmap.fromImage(image))
        self.ui.wound_healing_image.setScaledContents(True)
        self.ui.wound_healing_widget.setVisible(True)

    @Slot(QImage)
    def setImage_Original(self, image):
        self.history_n_n.photo_original = image_to_base64(image)
        self.image_original = QPixmap.fromImage(image)
        self.ui.wound_healing_image.setPixmap(QPixmap.fromImage(image))
        self.ui.wound_healing_image.setScaledContents(True)
        self.ui.wound_healing_widget.setVisible(True)

    @Slot(QPixmap)
    def setImage_Predict(self, image: QPixmap):
        # print(image)
        print('setImage_Predict')
        self.history_n_n.photo_predict = image_to_base64(image.toImage())
        self.ui.wound_healing_image.setPixmap(image)
        self.ui.wound_healing_image.setScaledContents(True)
        self.ui.wound_healing_widget.setVisible(True)
        self.ui.widget_2.setVisible(True)
        self.ui.wound_healing_loading_label.setText('Ok')


    @Slot(QPixmap)
    def setImage_Predict_edit(self, image: QPixmap):
        self.history_n_n.photo_predict_edit_doctor = image_to_base64(image.toImage())
        self.ui.wound_healing_image.setPixmap(image)
        self.ui.wound_healing_image.setScaledContents(True)
        self.ui.wound_healing_widget.setVisible(True)

    def start_scan(self):
        print('sss')
        self.hide_widget()
        self.unblock_result_scan_widget()
        self.history_n_n = HistoryNeuralNetwork()
        self.load_model_and_predict.play_video = False
        self.ui.wound_healing_loading_label.setVisible(True)
        self.load_model_and_predict.start()
        # self.load_model_and_predict.start()
        # self.ui.wound_healing_loading_label.setVisible(True)
        # self.l.get_random_image()
        # img2 = self.l.image_preprocessing()
        # self.l.create_batch(img2)
        # pred = self.l.predict()
        # convertToQtFormat = QImage(pred.data, pred.shape[1], pred.shape[0],
        #                            QImage.Format.Format_BGR888)
        # image_detect_qt_format = convertToQtFormat.scaled(256, 256, Qt.KeepAspectRatio)
        # self.ui.wound_healing_image.setPixmap(QPixmap.fromImage(image_detect_qt_format))
        # self.ui.wound_healing_image.setScaledContents(True)
        # self.result_scan()


if __name__ == '__main__':
    app = QApplication()
    window = WoundHealingPatient()
    window.show()
    sys.exit(app.exec())
