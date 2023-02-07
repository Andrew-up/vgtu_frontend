from dto.patientDTO import PatientDTO, getPatient, getPatientDTO, getPatientList
from model.patient_model import Patient
from controller.PatientController import get_all_patients, add_patient, delete_patient


class PatientServiceFront(object):

    def __init__(self, doctor_id):
        self.doctor = doctor_id

    def getAll(self):
        all_patients = get_all_patients(self.doctor)
        return all_patients

    def deletePatientById(self, id_patient):
        res = delete_patient(id_patient=id_patient)
        return res

    def add(self, patient: Patient) -> Patient:
        res = add_patient(patient)
        return res


