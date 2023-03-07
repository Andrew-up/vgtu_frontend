from model.result_predict import ResultPredict
from model.Annotations import Annotations

class HistoryNeuralNetwork:
    def __init__(self, **entries):
        self.id_history_neural_network = 0
        self.photo_original = None
        self.photo_predict = None
        self.photo_predict_edit_doctor = None
        self.healing_history_id: int = 0
        self.annotations: list[Annotations()] = []
        self.__dict__.update(entries)

