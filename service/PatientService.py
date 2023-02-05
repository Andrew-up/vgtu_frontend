from dto.patientDTO import PatientDTO, getPatient, getPatientDTO, getPatientList
from model.patient_model import Patient
from controller.PatientController import get_all_patients


class PatientServiceFront(object):

    def __init__(self, doctor_id):
        self.doctor = doctor_id

    def getAll(self):
        all_patients = get_all_patients(self.doctor)
        return all_patients

    def deletePatientById(self, id_patient):
        # patientService = PatientService(self.doctor)
        # res = patientService.deletePatientById(id_patient)
        return "Метод не работает"
