import cv2
from PySide6.QtCore import Slot, QSize, Qt
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtWidgets import QWidget, QApplication, QMessageBox, QFrame, QFileDialog
import sys
from view.py.wound_healing_widget import Ui_Form
from service.unetModelService import LoadingModelAndPredict
from matplotlib import pyplot as plt
from definitions import DATASET_PATH, MODEL_H5_PATH
from model.result_scan import ResultScan

class WoundHealingPatient(QWidget):

    def __init__(self, parent=None):
        super(WoundHealingPatient, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.patient_id = 0
        self.hide_widget()
        self.ui.wound_healing_start_scan.clicked.connect(self.start_scan)
        self.ui.radio_scan_to_photo_catalog.clicked.connect(self.on_radio_scan_from_catalog)
        self.ui.radio_scan_to_cam.clicked.connect(self.on_radio_scan_to_cam)
        self.ui.button_select_ptoho_from_catalog.setVisible(False)

        #------- Отдельный поток и связка сигналов
        self.load_model_and_predict = LoadingModelAndPredict(MODEL_H5_PATH)
        self.load_model_and_predict.setObjectName('LOAD_MODEL_THREAD')
        self.load_model_and_predict.loading_model_end.connect(self.on_load_model_end_signal)
        self.load_model_and_predict.image_original.connect(self.setImage)
        self.load_model_and_predict.predict_image_result.connect(self.setImage)
        self.load_model_and_predict.result_scan.connect(self.result_scan_init)
        # -------

        self.ui.button_select_ptoho_from_catalog.clicked.connect(self.open_file_from_catalog)
        self.test_color()


    def test_color(self):
        pass

    @Slot(ResultScan)
    def result_scan_init(self, res: list[ResultScan]):
        self.ui.wound_healing_type_wound.setText('Тип раны: <br>')
        self.ui.wound_healing_area_wound.setText('Площадь: <br>')
        self.ui.label_9.setText(f'<font style="color:rgb(255, 0, 0);"> КОНТУР РАНЫ НЕ ОПРЕДЕЛЕН </font>')
        for i in res:
                self.ui.label_9.setText(f'<font style="color:rgb(0, 255, 0);"> КОНТУР РАНЫ ОПРЕДЕЛЕН </font>')
                print(i.type_wound)
                print(i.color)
                self.ui.wound_healing_type_wound.setText(self.ui.wound_healing_type_wound.text() +
                                                         f'<font style="color:rgb{i.color};">{i.type_wound}</font>, ')

                self.ui.wound_healing_area_wound.setText(self.ui.wound_healing_area_wound.text() +
                                                         f'<font style="color:rgb{i.color};">{i.type_wound}</font>: {i.area_wound}, <br>')
                # self.ui.wound_healing_area_wound.setText(f'Площадь: {str(i.area_wound)}')



    def on_radio_scan_from_catalog(self):
        if self.ui.radio_scan_to_photo_catalog.isChecked():
            self.ui.button_select_ptoho_from_catalog.setVisible(True)
            self.load_model_and_predict.scan_from_cam = False
            self.ui.wound_healing_start_scan.setEnabled(False)

    def on_radio_scan_to_cam(self):
        if self.ui.radio_scan_to_cam.isChecked():
            self.load_model_and_predict.image_path = None
            self.ui.button_select_ptoho_from_catalog.setVisible(False)
            self.load_model_and_predict.scan_from_cam = True
            self.ui.wound_healing_start_scan.setEnabled(True)

    def hide_widget(self):
        self.ui.wound_healing_widget.setVisible(False)
        self.ui.wound_healing_loading_label.setVisible(False)
        self.ui.wound_healing_start_scan.setEnabled(False)

    def open_file_from_catalog(self):
        fileName = QFileDialog.getOpenFileName(self, ("Open Image"), DATASET_PATH,
                                               ("Image Files (*.png *.jpg, *.jpeg, *.tiff, *.*)"))
        self.ui.file_name_select_folder.setText(fileName[0])
        if fileName[0] != '':
            self.load_model_and_predict.image_path = fileName[0]
            self.ui.wound_healing_start_scan.setEnabled(True)

    @Slot(str)
    def on_load_model_end_signal(self, time_load_model):
        self.ui.wound_healing_loading_label.setText(f'Модель была загружена за {time_load_model} секунды \n '
                                                    f'Идет распознавание болезни \n'
                                                    f'подождите....')
        print('модель загружена')

    @Slot(QImage)
    def setImage(self, image):
        self.ui.wound_healing_image.setPixmap(QPixmap.fromImage(image))
        self.ui.wound_healing_image.setScaledContents(True)
        self.ui.wound_healing_widget.setVisible(True)

    def start_scan(self):
        self.load_model_and_predict.start()
        self.ui.wound_healing_loading_label.setVisible(True)
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

    def result_scan(self):
        self.ui.wound_healing_widget.setVisible(True)
        pass


if __name__ == '__main__':
    app = QApplication()
    window = WoundHealingPatient()
    window.show()
    sys.exit(app.exec())
