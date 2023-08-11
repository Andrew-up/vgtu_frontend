import base64
import sys
from ast import literal_eval
from io import BytesIO

from PIL import Image
from PySide6.QtCore import QByteArray
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtWidgets import QWidget, QApplication

from model.history_patient import HistoryPatient
from service.imageService import is_valid_base64_image
from view.py.history_patient_item_widget import Ui_Form
from view.user.more_history_patient_item import MoreHistoryPatientItem


class HistoryPatientWidgetItem(QWidget):

    def __init__(self, history: HistoryPatient() = None, parent=None):
        super(HistoryPatientWidgetItem, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.patient_id = 0
        self.history_patient: HistoryPatient = history
        self.init_history_item()
        self.ui.pushButton.clicked.connect(self.open_more_history_item)

    def open_more_history_item(self):
        dlg = MoreHistoryPatientItem(self.history_patient)
        dlg.exec()

    def init_history_item(self):
        if self.history_patient is not None:
            self.ui.patient_history_item_comment.setText(self.history_patient.comment)
            self.ui.patient_history_item_date.setText(self.history_patient.date)
            photo = self.history_patient.history_neutral_network.photo_predict
            photo_pred = self.history_patient.history_neutral_network.photo_predict_edit_doctor
            img = is_valid_base64_image(photo)
            img_pred = is_valid_base64_image(photo_pred)
            if img_pred:
                image_bytes = base64.b64decode(photo_pred)
                img = QImage.fromData(image_bytes)
                image = QPixmap.fromImage(img)
                self.ui.patient_history_item_image.setPixmap(image)
                self.ui.patient_history_item_image.setScaledContents(True)
                print('img_pred')
                return 0

            if img:
                image_bytes = base64.b64decode(photo)
                img = QImage.fromData(image_bytes)
                image = QPixmap.fromImage(img)
                self.ui.patient_history_item_image.setPixmap(image)
                self.ui.patient_history_item_image.setScaledContents(True)
                print('img')


if __name__ == '__main__':
    app = QApplication()
    window = HistoryPatientWidgetItem()
    window.show()
    sys.exit(app.exec())
