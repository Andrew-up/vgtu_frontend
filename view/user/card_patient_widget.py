from PySide6.QtCore import Slot, QSize
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtWidgets import QWidget, QApplication, QMessageBox, QFrame
import sys
from PySide6.QtCore import QThread, Signal, Qt
from model.patient_model import Patient
from service.slotsService import SlotsMainMenu
from view.py.card_patient_widget import Ui_Form
from datetime import date, datetime
from service.generate_random_repson import generate_person
from service.PatientService import PatientServiceFront

ID_DOCTOR = 1


class CardPatient(QWidget):

    def __init__(self, patient: Patient = None, parent=None):
        super(CardPatient, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.patient = patient
        self.ui.delete_patient_button.clicked.connect(self.delete_patient)
        self.main_menu_slots = None
        self.main_menu_slots: SlotsMainMenu
        self.init_card_patient()

    def set_main_menu_slots(self, value: SlotsMainMenu):
        print('CARD PATIENT SLOTS: ')
        self.main_menu_slots = value
        print(self.get_main_menu_slots())

    def get_main_menu_slots(self) -> SlotsMainMenu:
        return self.main_menu_slots

    def delete_patient(self):
        if self.get_main_menu_slots() is not None:
            print('11111111111111')
        else:
            print('2222222222222')

        msg = QMessageBox()
        msg.setInformativeText(f"Удалить пациента {self.patient.full_name}\n"
                               f"id: {self.patient.id_patient} ? \n"
                               f"Удаление отменить невозможно.")
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setWindowTitle("Удаление пациента")
        msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)
        res = msg.exec()
        if res == QMessageBox.StandardButton.Yes:
            print('Удаляем')
            p = PatientServiceFront(ID_DOCTOR)
            print(self.patient.id_patient)
            p.deletePatientById(self.patient.id_patient)
            if self.get_main_menu_slots() is not None:
                print('11111111111111')
                self.get_main_menu_slots().open_start_view.emit()
                self.close()
            else:
                print('2222222222222')
                self.close()
        if res == QMessageBox.StandardButton.Cancel:
            print('Отмена удаления')

    def init_card_patient(self):
        patient = self.patient
        if patient.full_name is not None:
            self.ui.card_fullname_patient.setText(patient.full_name)
        if patient.date_of_birth is not None:
            self.ui.card_date_birth_patient.setText('Дата рождения: ' + str(patient.date_of_birth))
            patient_datetime = datetime.strptime(str(patient.date_of_birth), '%Y-%m-%d').date()
            self.ui.card_age_patient.setText('Возраст: ' + str(self.get_age(patient_datetime)))
        if patient.polis_oms is not None:
            self.ui.card_oms_patient.setText('Полис ОМС: ' + patient.polis_oms)
        if patient.document is not None:
            self.ui.card_document_patient.setText('Документ: ' + patient.document)
        if patient.phone is not None:
            self.ui.card_phone_patient.setText('Телефон: ' + patient.phone)
        if patient.snils is not None:
            self.ui.card_snils_patient.setText('Снилс: ' + patient.snils)
        if patient.address is not None:
            self.ui.card_address_patient.setText('Адрес: ' + patient.address)
        if patient.gender is not None:
            if patient.gender == 'male':
                self.ui.card_gender_patient.setText('Пол: мужский')
            if patient.gender == 'female':
                self.ui.card_gender_patient.setText('Пол: женский')

    def get_age(self, birthday):
        today = date.today()
        age = today.year - birthday.year
        if today.month < birthday.month:
            age -= 1
        elif today.month == birthday.month and today.day < birthday.day:
            age -= 1
        return age


if __name__ == '__main__':
    app = QApplication()
    p = generate_person()
    window = CardPatient(p)
    window.show()
    sys.exit(app.exec())
