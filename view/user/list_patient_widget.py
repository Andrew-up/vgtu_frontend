from PySide6.QtCore import Slot, QSize, Signal
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtWidgets import QWidget, QApplication, QMessageBox, QFrame, QStackedWidget
import sys
from view.py.list_patient_widget import Ui_Form
from view.user.list_patient_table_widget import ListPatientItem
from service.generate_random_repson import generate_person
from service.PatientService import PatientServiceFront
from model.patient_model import Patient
from view.user.patient_registration_widget import PatientRegistration
from service.slotsService import SlotsMainMenu


class ListPatient(QWidget):

    def __init__(self, parent=None):
        super(ListPatient, self).__init__(parent)
        self.patient_list = None
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_8.clicked.connect(self.add_new_patient)
        self.patient_list: list[Patient]
        self.ui.update_patients.clicked.connect(self.on_update_list)
        self.main_menu_slots = None
        self.main_menu_slots: SlotsMainMenu

    def set_main_menu_slots(self, value: SlotsMainMenu):
        self.main_menu_slots = value
        pass

    def get_main_menu_slots(self) -> SlotsMainMenu:
        return self.main_menu_slots

    def on_update_list(self):
        self.patient_list = None
        for i in reversed(range(self.ui.verticalLayout_4.count())):
            self.ui.verticalLayout_4.itemAt(i).widget().setParent(None)
        self.get_all_patient()

    def get_all_patient(self):
        service = PatientServiceFront(1)
        self.patient_list = service.getAll()

        if self.patient_list is not None:
            for patient in self.patient_list:
                print(patient.full_name)
                new = ListPatientItem(patient=patient)
                new.set_main_menu_slots(self.get_main_menu_slots())
                self.ui.verticalLayout_4.addWidget(new)



    def add_new_patient(self, patient: Patient = 0):
        dlg = PatientRegistration()
        dlg.exec()
        pass


if __name__ == '__main__':
    app = QApplication()
    window = ListPatient()
    window.show()
    sys.exit(app.exec())
