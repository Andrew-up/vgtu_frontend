import requests

from dto.patientDTO import PatientDTO, getPatient, getPatientDTO
from model.history_patient import HistoryPatient
from model.patient_model import Patient
from model.result_predict import ResultPredict
from utils.read_xml_file import ReadXmlProject

SECRET_KEY = {"key": 'hFGHFEFyr67ggghhPJhdfh123dd'}
api = ReadXmlProject().get_API() + 'api/'


def get_patient_by_id(id: int) -> Patient:
    r = requests.get(f'{api}patient/{id}/')
    dto: PatientDTO = PatientDTO(**r.json())
    p: Patient() = getPatient(dto)
    print(f'ответ от сервера за : {r.elapsed.total_seconds()} секунд')
    return p


def get_all_patients(id_doctor: int) -> list[Patient]:
    api_full = f'{api}all/'
    print(api_full)
    r = requests.get(api_full)
    if r.status_code == 200:
        patients: list[Patient] = []
        for dto_dict in r.json():
            p = Patient()
            dto = PatientDTO(**dto_dict)
            patient: Patient = getPatient(dto)
            patients.append(patient)
        return patients


def get_history_patient(id_patient) -> list[HistoryPatient]:
    r = requests.get(f'{api}patient/history/{id_patient}/')
    h = r.json()
    list_history_patient: list[HistoryPatient] = []
    for i in h:
        one_obj = HistoryPatient(**i).set_dict()
        print(one_obj)
        list_history_patient.append(one_obj)
    return list_history_patient


def add_patient(patient: Patient):
    dto: PatientDTO = getPatientDTO(patient)
    api_full = f'{api}add/'
    print(api_full)
    r = requests.post(api_full, json=dto.__dict__, headers={"Content-Type": "application/json"})
    print(f'ответ от сервера за : {r.elapsed.total_seconds()} секунд')
    dto_new = PatientDTO(**r.json())
    new_patient = getPatient(dto_new)
    return new_patient


def delete_patient(id_patient):
    str = f'{api}patient/delete/{id_patient}'
    r = requests.post(str, json=SECRET_KEY, headers={"Content-Type": "application/json"})
    # print(r.text)
    return r.text


def add_history_patient(history: HistoryPatient):
    str_api = f'{api}/history/add/{history.patient_id}/'
    json = history.__dict__
    print(json)
    r = requests.post(str_api, json=json, headers={"Content-Type": "application/json"})
    return r.status_code, r.text


def get_categorical_predict() -> list[ResultPredict]:
    str_api = f'{api}/categorical/all/'
    r = requests.get(str_api)
    result_predict_list: list[ResultPredict] = []
    for i in r.json():
        result_predict_list.append(ResultPredict(**i))
    return result_predict_list


if __name__ == '__main__':
    # h = HistoryPatient()
    # h.comment = 'test'
    # h_nn = HistoryNeuralNetwork()
    # h_nn.id_history_neural_network = 1
    # res = ResultPredict()
    # res.name_category_ru = '1234'
    # h.history_neutral_network = h_nn
    #
    # a = Annotations()
    # a.segmentation = "123,123,123,123123"
    # a.bbox = "[123,123,22,33]"
    # h.history_neutral_network.annotations.append(a)
    # h.history_neutral_network.annotations.append(a)
    # h.history_neutral_network.annotations.append(a)
    # # h.history_neutral_network.annotations = h.history_neutral_network.annotations
    # h.history_neutral_network.result_predict = res
    # h.history_neutral_network = h.history_neutral_network
    # print(get_history_Json(h))

    get_history_patient(1)

    # delete_patient(10)
#     # get_patient_by_id(30)
#     # l = get_all_patients(1)
#     # print(l[0].id_patient)
#     # p = Patient()
#     # p.firstname = "123"
#     # add_patient(p)
#     # get_patient_by_id(1)
#     # get_history_patient(5)
#     # p = Patient()
#     # p.address = "123"
#     # add_patient(p)
#     # print(get_categorical_predict())
#     pass
