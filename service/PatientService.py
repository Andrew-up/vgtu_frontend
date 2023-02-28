from dto.patientDTO import PatientDTO, getPatient, getPatientDTO, getPatientList
from model.patient_model import Patient
from model.history_patient import HistoryPatient
from controller.PatientController import get_patient_by_id,\
    get_all_patients, add_patient, delete_patient, get_history_patient, add_history_patient, get_categorical_predict


class PatientServiceFront(object):

    def __init__(self, doctor_id=1):
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

    def getHistoryPatient(self, id_patient):
        history = get_history_patient(id_patient=id_patient)
        return history

    def getPatientById(self, id_patient) -> Patient:
        patient = get_patient_by_id(id_patient)
        return patient

    def addHistoryPatient(self, history: HistoryPatient):
        status_code, text = add_history_patient(history)
        return status_code, text


    def get_all_categorical(self):
        return get_categorical_predict()


