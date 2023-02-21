from PySide6.QtCore import Slot, QSize
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtWidgets import QWidget, QApplication, QMessageBox, QFrame,QDialog
import sys
from view.py.history_patient_item_widget import Ui_Form
from model.history_patient import HistoryPatient
from service.imageService import image_to_base64, base64_to_image, is_valid_base64_image

class HistoryPatientWidgetItem(QWidget):

    def __init__(self, history: HistoryPatient() = None, parent=None):
        super(HistoryPatientWidgetItem, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.patient_id = 0
        self.history_patient: HistoryPatient = history
        self.init_history_item()

    def init_history_item(self):
        if self.history_patient is not None:
            self.ui.patient_history_item_comment.setText(self.history_patient.comment)
            self.ui.patient_history_item_date.setText(self.history_patient.date)
            photo = self.history_patient.history_neutral_network.photo_original
            img = is_valid_base64_image(photo)
            if img:
                ssss = base64_to_image(photo)
                image = QPixmap.fromImage(ssss)
                self.ui.patient_history_item_image.setPixmap(image)
                self.ui.patient_history_item_image.setScaledContents(True)



if __name__ == '__main__':
    app = QApplication()
    window = HistoryPatientWidgetItem()
    window.show()
    sys.exit(app.exec())
