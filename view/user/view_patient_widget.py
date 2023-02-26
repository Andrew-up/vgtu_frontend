import sys

from PySide6.QtWidgets import QApplication, QDialog

from model.patient_model import Patient
from service.PatientService import PatientServiceFront
from service.slotsService import SlotsMainMenu
from view.py.view_patient_widget import Ui_Form
from view.user.card_patient_widget import CardPatient
from view.user.history_patient_widget import HistoryPatient
from view.user.wound_treatment_widget import WoundHealingPatient

class ViewPatient(QDialog):

    def __init__(self, patient: Patient = None, parent=None):
        super(ViewPatient, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.view_patient_go_mainmenu.clicked.connect(self.close_view_patient)
        self.ui.view_patient_go_card_patient.clicked.connect(self.on_click_card_patient)
        self.ui.view_patient_go_history_healing.clicked.connect(self.on_click_history_patient)
        self.ui.view_patient_go_wound_treatment.clicked.connect(self.on_click_wound_treatment_patient)
        self.card_patient = CardPatient(patient)
        self.history_widget = HistoryPatient(patient)
        self.wound_treatment_widget = WoundHealingPatient(patient=patient)
        self.patient = patient
        self.main_menu_slots = None
        self.main_menu_slots: SlotsMainMenu
        self.ui.stacked_widget_view_patient.addWidget(self.card_patient)
        self.ui.stacked_widget_view_patient.addWidget(self.history_widget)
        self.ui.stacked_widget_view_patient.addWidget(self.wound_treatment_widget)



    def set_main_menu_slots(self, value: SlotsMainMenu):
        self.main_menu_slots = value
        self.ui.view_patient_go_card_patient.setFocus()
        self.ui.view_patient_go_card_patient.click()

    def get_main_menu_slots(self):
        return self.main_menu_slots

    def clear_stacked_widget(self):
        pages = self.ui.stacked_widget_view_patient.count()
        for i in range(pages):
            widget = self.ui.stacked_widget_view_patient.widget(0)
            self.ui.stacked_widget_view_patient.removeWidget(widget)
        print('очистка')

    def close_view_patient(self):
        if self.get_main_menu_slots() is not None:
            self.clear_stacked_widget()
            print('Открыть главное меню')
            self.get_main_menu_slots().open_start_view.emit()

    def on_click_card_patient(self):
        self.card_patient.set_main_menu_slots(self.get_main_menu_slots())
        self.ui.stacked_widget_view_patient.setCurrentWidget(self.card_patient)
        print('открыть карту пациента в родительском виджете')

    def on_click_history_patient(self):
        print(self.ui.stacked_widget_view_patient.count())
        self.ui.stacked_widget_view_patient.setCurrentWidget(self.history_widget)
        self.history_widget.update_list_patient()
        print('открыть историю лечения пациента')

    def on_click_wound_treatment_patient(self):
        self.ui.stacked_widget_view_patient.setCurrentWidget(self.wound_treatment_widget)
        print('открыть обработку раны пациента')


if __name__ == '__main__':
    app = QApplication()
    p = PatientServiceFront()
    patient = p.getPatientById(4)
    window = ViewPatient(patient)
    window.show()
    sys.exit(app.exec())
