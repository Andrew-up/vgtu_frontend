import base64
import sys
from ast import literal_eval

from PySide6.QtWidgets import QWidget, QApplication, QDialog

from model.history_patient import HistoryPatient
from view.py.more_history_patient_item import Ui_Form
from service.imageService import image_to_base64, base64_to_image, is_valid_base64_image, byteArrayToPixmap, stringIsBase64


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
        img_orig = is_valid_base64_image(self.history_patient.history_neutral_network.photo_original)
        img_pred = is_valid_base64_image(self.history_patient.history_neutral_network.photo_predict)
        img_pred_edit = is_valid_base64_image(self.history_patient.history_neutral_network.photo_predict_edit_doctor)
        polygon = stringIsBase64(self.history_patient.history_neutral_network.polygon_mask)
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

        print(polygon)
        if polygon:
            s = self.history_patient.history_neutral_network.polygon_mask
            res = base64.b64decode(literal_eval(s)).decode('utf-8')
            self.ui.label_polygon.setWordWrap(True)
            self.ui.label_polygon.setText(str(res))

        self.ui.label_date.setText(self.history_patient.date)
        self.ui.label_comment.setText(self.history_patient.comment)
        print(self.history_patient.history_neutral_network.result_predict)
        if self.history_patient.history_neutral_network.result_predict is not None:
            self.ui.label_dianosis.setText(self.history_patient.history_neutral_network.result_predict.name_category_ru)

        # print(img_orig)
        # print(img_pred)
        # print(img_pred_edit)



if __name__ == '__main__':
    app = QApplication()
    window = MoreHistoryPatientItem()
    window.show()
    sys.exit(app.exec())
