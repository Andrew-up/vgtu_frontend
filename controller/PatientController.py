import time

import requests
import json

from dto.patientDTO import PatientDTO, getPatient, getPatientDTO
from model.patient_model import Patient

IpV4 = '188.235.18.191'
port = 8095
API = f'http://{IpV4}:{port}/api/'
SECRET_KEY = {"key": 'hFGHFEFyr67ggghhPJhdfh123dd'}

def get_patient_by_id(id: int) -> Patient:


    # start = time.time()
    r = requests.get(f'{API}patient/{id}/')
    # r = requests.get('http://localhost:5000/api/patient/10/')

    print(r.url)
    dto: PatientDTO = PatientDTO(**r.json())

    p: Patient() = getPatient(dto)
    # print(f'ответ от сервера за : {r.elapsed.total_seconds()} секунд')

    return p


def get_all_patients(id_doctor: int) -> list[Patient]:
    start = time.time()
    api_full = f'{API}all/'
    r = requests.get(api_full)
    roundtrip = time.time() - start
    # print(f'ответ от сервера за : {r.elapsed.total_seconds()} секунд')
    # print(f'ответ от сервера за : {roundtrip} секунд')
    if r.status_code == 200:
        patients: list[Patient] = []
        for dto_dict in r.json():
            p = Patient()
            dto = PatientDTO(**dto_dict)
            patient: Patient = getPatient(dto)
            patients.append(patient)
            # print(patient.full_name)
        return patients


def add_patient(patient: Patient):
    dto: PatientDTO = getPatientDTO(patient)
    api_full = f'{API}add/'
    print(api_full)
    r = requests.post(api_full, json=dto.__dict__, headers={"Content-Type": "application/json"})
    print(f'ответ от сервера за : {r.elapsed.total_seconds()} секунд')
    dto_new = PatientDTO(**r.json())
    new_patient = getPatient(dto_new)
    return new_patient

def delete_patient(id_patient):
    str = f'{API}patient/delete/{id_patient}'
    r = requests.post(str, json=SECRET_KEY, headers={"Content-Type": "application/json"})
    # print(r.text)
    return r.text

if __name__ == '__main__':

    # delete_patient(10)
    # get_patient_by_id(30)
    # l = get_all_patients(1)
    # print(l[0].id_patient)
    p = Patient()
    p.firstname = "123"
    add_patient(p)

    # p = Patient()
    # p.address = "123"
    # add_patient(p)

    pass
