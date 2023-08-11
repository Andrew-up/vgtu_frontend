import sys
from ast import literal_eval

from PySide6.QtWidgets import QApplication, QDialog

from model.history_patient import HistoryPatient
from service.imageService import is_valid_base64_image, byteArrayToPixmap
from utils.read_xml_file import ReadXmlProject
from view.py.more_history_patient_item import Ui_Form


class MoreHistoryPatientItem(QDialog):

    def __init__(self, history: HistoryPatient() = None, parent=None):
        super(MoreHistoryPatientItem, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.history_patient: HistoryPatient = history
        if history is not None:
            self.initImage()
        self.ui.button_close.clicked.connect(self.close_this)

    def close_this(self):
        self.close()

    def initImage(self):
        coefficient_k = ReadXmlProject().get_coefficient_k
        img_orig = is_valid_base64_image(self.history_patient.history_neutral_network.photo_original)
        img_pred = is_valid_base64_image(self.history_patient.history_neutral_network.photo_predict)
        img_pred_edit = is_valid_base64_image(self.history_patient.history_neutral_network.photo_predict_edit_doctor)
        if img_orig:
            pixmap_orig = byteArrayToPixmap(self.history_patient.history_neutral_network.photo_original)
            self.ui.image_original.setPixmap(pixmap_orig)
            self.ui.image_original.setScaledContents(True)
        if img_pred:
            pixmap_pred = byteArrayToPixmap(self.history_patient.history_neutral_network.photo_predict)
            self.ui.image_predict.setPixmap(pixmap_pred)
            self.ui.image_predict.setScaledContents(True)
        if img_pred_edit:
            pixmap_pred_edit = byteArrayToPixmap(self.history_patient.history_neutral_network.photo_predict_edit_doctor)
            self.ui.image_predict_edit_doctor.setPixmap(pixmap_pred_edit)
            self.ui.image_predict_edit_doctor.setScaledContents(True)

        if self.history_patient.history_neutral_network:
            if self.history_patient.history_neutral_network.annotations:
                string_dianosis = str()
                for i in self.history_patient.history_neutral_network.annotations:
                    r, g, b = literal_eval(i.result_predict.color)
                    string_dianosis += f' <font style="color:rgb({r}, {g}, {b});"> ' \
                                       f'Категория: {i.result_predict.name_category_ru}' f' ' \
                                       f'Площадь: {str(float(round(i.area * coefficient_k, 2)))} кв мм' \
                                       f' Полигон: {i.segmentation} <br> ____________________ <br></font>'
                self.ui.label_dianosis.setWordWrap(True)
                self.ui.label_dianosis.setText(string_dianosis)
                # self.ui.label_dianosis.setText('______________________________________')

        self.ui.label_date.setText(self.history_patient.date)
        self.ui.label_comment.setText(self.history_patient.comment)


if __name__ == '__main__':
    app = QApplication()
    window = MoreHistoryPatientItem()
    window.show()
    sys.exit(app.exec())
