import datetime
import os
import sys
import time
from itertools import groupby

from PySide6.QtCore import Slot
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtWidgets import QWidget, QApplication, QFileDialog

from definitions import DATASET_PATH
from model.Annotations import Annotations
from model.history_neural_network import HistoryNeuralNetwork
from model.history_patient import HistoryPatient
from model.patient_model import Patient
from service.PatientService import PatientServiceFront
from service.imageService import image_to_base64
from service.unetModelService import LoadingModelAndPredict
from utils.message_box import message_error_show, message_info_show
from utils.read_xml_file import ReadXmlProject
from view.py.wound_healing_widget import Ui_Form


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
        xml2 = ReadXmlProject()
        path_model = os.path.join(xml2.get_root_dir, xml2.model_cnn_path)
        path_model_and_name = os.path.join(path_model, xml2.model_cnn_name)
        print(path_model_and_name)
        self.load_model_and_predict = LoadingModelAndPredict(path_model_and_name)
        self.load_model_and_predict.setObjectName('LOAD_MODEL_THREAD')
        self.load_model_and_predict.loading_model_end.connect(self.on_load_model_end_signal)
        self.load_model_and_predict.image_original.connect(self.setImage_Original)
        self.load_model_and_predict.video_stream_image.connect(self.playVideoStream)
        self.load_model_and_predict.predict_image_result.connect(self.setImage_Predict)
        self.load_model_and_predict.result_scan.connect(self.result_scan_init)
        self.load_model_and_predict.set_categorical_predict(self.get_predict_categorical())
        # print(self.load_model_and_predict.categorical_predict)
        # -------
        self.ui.label.setText(f'Используется {xml2.model_cnn_version} версия нейронной сети')

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

        self.index_cam = -1

    def get_predict_categorical(self):
        return PatientServiceFront(1).get_all_categorical()

    def on_result_is_ok(self):
        history = HistoryPatient()
        history.date = str(datetime.datetime.now())
        history.comment = 'тест'
        history.patient_id = self.patient_id
        history.history_neutral_network = self.history_n_n

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
        from view.user.drawing_counter import DrawingCounter
        dlg = DrawingCounter(self.image_original)
        dlg.image_result_edit_doctor.connect(self.setImage_Predict_edit)
        dlg.annotation_signal.connect(self.result_scan_init)
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

    @Slot(Annotations)
    def result_scan_init(self, annotation_list: list[Annotations]):
        print('result_scan_init')
        self.ui.wound_healing_type_wound.setText('Тип раны: <br>')
        self.ui.wound_healing_area_wound.setText('Площадь: <br>')
        self.ui.label_9.setText(f'<font style="color:rgb(255, 0, 0);"> КОНТУР РАНЫ НЕ ОПРЕДЕЛЕН </font>')
        coefficient_k = ReadXmlProject().get_coefficient_k
        string_res = str()

        if annotation_list:
            self.history_n_n.annotations = annotation_list
            self.ui.label_9.setText(
                f'<font style="color:rgb(0, 255, 0);"> Определен {len(annotation_list)} контур(а) </font>')
            sort_list = sorted(annotation_list, key=lambda x: x.category_id)
            for key, groups_item in groupby(sort_list, key=lambda x: x.category_id):
                sum = 0.0
                category_ru: str = str()
                color = (255, 255, 255)
                for item in groups_item:
                    sum += item.area
                    category_ru = item.result_predict.name_category_ru
                    color = item.result_predict.color
                    print(item.result_predict.color)
                string_res += f'<font style="color:rgb{color};">  {category_ru} {str(round(float(sum * coefficient_k), 2))}</font>, '
            self.ui.wound_healing_area_wound.setText('Площадь: <br>' + string_res + '<br>')
            self.ui.wound_healing_area_wound.setWordWrap(True)

    @Slot(int)
    def set_cam_index(self, index: int):
        self.index_cam = index

    def on_radio_scan_from_catalog(self):
        if self.ui.radio_scan_to_photo_catalog.isChecked():
            self.ui.button_select_ptoho_from_catalog.setVisible(True)
            self.load_model_and_predict.play_video = False
            self.load_model_and_predict.scan_from_cam = False
            self.ui.wound_healing_start_scan.setEnabled(False)
            self.set_cam_index(-1)
            self.load_model_and_predict.quit()
            self.ui.file_name_select_folder.setText("Выберите фото из каталога")

    def on_radio_scan_to_cam(self):
        from view.user.selected_index_cam_widget import SelectedCamera
        if self.index_cam == -1:
            selected = SelectedCamera()
            selected.clickButtonItem.connect(self.set_cam_index)
            selected.exec()

        if self.ui.radio_scan_to_cam.isChecked():
            self.load_model_and_predict.image_path = None
            self.ui.button_select_ptoho_from_catalog.setVisible(False)
            self.load_model_and_predict.scan_from_cam = True
            self.load_model_and_predict.play_video = True
            self.ui.file_name_select_folder.setText("Выберите камеру из списка")
            if self.index_cam >= 0:
                self.load_model_and_predict.number_cam = self.index_cam
                self.load_model_and_predict.start()
                self.ui.wound_healing_start_scan.setEnabled(True)
                self.ui.file_name_select_folder.setText(f"Выбрана камера: {self.index_cam}")

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
            image = self.load_model_and_predict.get_image()
            height, width, channel = image.shape
            bytesPerLine = 3 * width
            image = QImage(image, width, height, bytesPerLine, QImage.Format_BGR888)
            self.setImage_Original(QPixmap(image))
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
    def setImage_Original(self, image: QPixmap):
        print(type(image))
        self.history_n_n.photo_original = image_to_base64(image.toImage())
        self.image_original = image
        print('111111111')
        self.ui.wound_healing_image.setPixmap(image)
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


if __name__ == '__main__':
    app = QApplication()
    window = WoundHealingPatient()
    window.show()
    sys.exit(app.exec())
