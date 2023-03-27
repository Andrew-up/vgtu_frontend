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




if __name__ == '__main__':
    print(get_history_training_model())