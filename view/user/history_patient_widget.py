from PySide6.QtCore import Slot, QSize
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtWidgets import QWidget, QApplication, QMessageBox, QFrame
import sys
from view.py.history_patient_widget import Ui_Form

class HistoryPatient(QWidget):

    def __init__(self, parent=None):
        super(HistoryPatient, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.patient_id = 0


if __name__ == '__main__':
    app = QApplication()
    window = HistoryPatient()
    window.show()
    sys.exit(app.exec())
