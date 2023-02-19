from PySide6.QtCore import Slot, QSize
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtWidgets import QWidget, QApplication, QMessageBox, QFrame
import sys
from view.py.history_patient_widget import Ui_Form
from view.user.history_patient_wodget_item import HistoryPatientWidgetItem
from service.PatientService import PatientServiceFront
from model.patient_model import Patient
class HistoryPatient(QWidget):

    def __init__(self, patient: Patient = None, parent=None):
        super(HistoryPatient, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.patient_id = 0
        self.items_layout = self.ui.history_patient_layout_list_healing
        self.item_size = 200
        self.ui.history_patient_button_next.clicked.connect(self.scroll_next)
        self.ui.history_patient_button_prev.clicked.connect(self.scroll_prev)
        self.history_patient: list[HistoryPatient] = []
        if patient is not None:
            self.init(patient)

    def init(self, patient:Patient):
        s = PatientServiceFront(1)
        self.history_patient = s.getHistoryPatient(patient.id_patient)
        self.ui.history_patient_fullname_patient.setText(patient.full_name)
        self.ui.history_patient_diagnosis_patient.setText(patient.dianosis)
        for i in self.history_patient:
            item = HistoryPatientWidgetItem()
            item.ui.patient_history_item_comment.setText(f'Test: {i.comment}')
            self.items_layout.addWidget(item)

    def scroll_next(self):
        self.ui.scrollArea.horizontalScrollBar().setValue(self.ui.scrollArea.horizontalScrollBar().value() + self.item_size)
    def scroll_prev(self):
        self.ui.scrollArea.horizontalScrollBar().setValue(self.ui.scrollArea.horizontalScrollBar().value() - self.item_size)


    def add_item(self):
        for i in range(10):
            item = HistoryPatientWidgetItem()
            item.ui.patient_history_item_comment.setText(f'Test: {i}')
            w = item.size().width()
            self.item_size = w
            self.items_layout.addWidget(item)



if __name__ == '__main__':
    p = PatientServiceFront()
    patient = p.getPatientById(5)
    app = QApplication()
    window = HistoryPatient(patient)
    window.show()
    sys.exit(app.exec())
