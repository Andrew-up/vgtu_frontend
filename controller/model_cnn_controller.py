from utils.read_xml_file import ReadXmlProject
from model.history_training_model import HistoryTrainingModel
import requests


api = ReadXmlProject().get_API() + 'api/'

def get_history_training_model():
    r = requests.get(f'{api}model_cnn/history/all/')
    list_request = r.json()
    list_history = []
    for i in list_request:
        list_history.append(HistoryTrainingModel(**i))
    print(f'ответ от сервера за : {r.elapsed.total_seconds()} секунд')
    return list_history


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