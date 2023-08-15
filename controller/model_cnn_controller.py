import requests

from model.history_training_model import HistoryTrainingModel
from utils.read_xml_file import ReadXmlProject

SECRET_KEY = {"key": 'hFGHFEFyr67ggghhPJhdfh123dd'}
api = ReadXmlProject().get_API() + 'api/'


def get_history_training_model():
    r = requests.get(f'{api}model_cnn/history/all/')
    list_request = r.json()
    list_history = []
    for i in list_request:
        list_history.append(HistoryTrainingModel(**i))
    print(f'ответ от сервера за : {r.elapsed.total_seconds()} секунд')
    return list_history


def delete_model_by_id(id: str):
    r = requests.post(f'{api}model_cnn/delete/{id}', json=SECRET_KEY, headers={"Content-Type": "application/json"})
    print(r.text)

def get_model_by_id(id: str):
    r = requests.get(f'{api}model_cnn/{id}')
    return r.json()

def get_last_history_training():
    r = requests.get(f'{api}model_cnn/last_model/')
    last_model_history = r.json()
    return last_model_history


def send_retraining_model():
    r = requests.get(f'{api}model_cnn/train/')
    train_json = r.json()
    return train_json


def get_annotation_json():
    api = ReadXmlProject().get_API() + 'api/ann_json/'
    r = requests.get(api)
    return r.json()


if __name__ == '__main__':
    get_history_training_model()
