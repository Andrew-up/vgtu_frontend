import sys
from PySide6.QtWidgets import QWidget, QApplication, QStackedWidget

from service.slotsService import SlotsMainMenu
from view.py.patient_table_item import Ui_Form
from view.user.view_patient_widget import ViewPatient
from PySide6.QtCore import QSize
from model.patient_model import Patient

class ListPatientItem(QWidget):

    def __init__(self, patient: Patient() = None, parent=None):
        super(ListPatientItem, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.patient = patient
        self.add_patient()
        self.ui.patient_table_item_fullname.clicked.connect(self.open_patient)
        self.ui.patient_table_item_snils.clicked.connect(self.open_patient)
        self.main_menu_slots = None
        self.main_menu_slots: SlotsMainMenu

    def set_main_menu_slots(self, value: SlotsMainMenu):
        self.main_menu_slots = value

    def get_main_menu_slots(self) -> SlotsMainMenu:
        return self.main_menu_slots

    def add_patient(self):
        self.ui.patient_table_item_fullname.setText(self.patient.full_name)
        self.ui.patient_table_item_snils.setText(self.patient.snils)

    def open_patient(self):
        vp = ViewPatient(patient=self.patient)
        if self.get_main_menu_slots() is not None:
            vp.set_main_menu_slots(self.get_main_menu_slots())
            self.get_main_menu_slots().set_widget_main_menu.emit(vp)
            print('hhhhhhhhh: '+str(vp.get_main_menu_slots()))
        else:
            vp.exec()


if __name__ == '__main__':
    app = QApplication()
    patient_test = Patient()
    patient_test.id_patient = 1
    patient_test.firstname = 'Иван'
    patient_test.last_name = 'Иванов'
    patient_test.middle_name = 'Иванович'
    print(patient_test.full_name)
    # patient.
    window = ListPatientItem(patient_test)
    window.show()
    sys.exit(app.exec())
