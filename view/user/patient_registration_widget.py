import sys

from PySide6.QtWidgets import QApplication, QMessageBox, QDialog

from model.patient_model import Patient
from service.PatientService import PatientServiceFront
from service.generate_random_repson import generate_person
from view.py.patient_registration import Ui_Form


class PatientRegistration(QDialog):

    def __init__(self, parent=None):
        super(PatientRegistration, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.patient: Patient = Patient()
        self.ui.get_random_patient_button.clicked.connect(self.get_random_person)
        self.ui.registration_button.clicked.connect(self.on_registration_button)
        self.ui.clear_all_button.clicked.connect(self.clear_all)

    def registration_ok(self, id_new_user: Patient):
        dlg = QMessageBox(self)
        dlg.setWindowTitle('Регистрация успешна! ')
        dlg.setText(f'Id нового пользователя: {id_new_user.id_patient}\n')
        dlg.setIcon(QMessageBox.Icon.Information)
        dlg.exec()

    def clear_all(self):
        pass

    def fill_registration_card(self):
        self.ui.firstname_patient.setText(self.patient.firstname)
        self.ui.lastname_patient.setText(self.patient.surname)
        self.ui.middle_name_patient.setText(self.patient.middlename)
        self.ui.date_of_birth_patient.setDate(self.patient.date_of_birth)
        self.ui.address_patient.setText(self.patient.address)
        self.ui.phone_patient.setText(self.patient.phone)
        self.ui.polis_oms_patient.setText(self.patient.polis_oms)
        self.ui.document_patient.setText(self.patient.document)
        self.ui.snils_patient.setText(self.patient.snils)

    def on_registration_button(self):
        p = PatientServiceFront(1)
        res: Patient = p.add(self.patient)
        if res:
            self.close()

    def get_random_person(self):
        patient_random: Patient = generate_person()
        self.patient = patient_random
        self.fill_registration_card()


if __name__ == '__main__':
    app = QApplication()
    window = PatientRegistration()
    window.show()
    sys.exit(app.exec())
