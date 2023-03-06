from model.history_neural_network import HistoryNeuralNetwork
from model.Annotations import Annotations
from model.result_predict import  ResultPredict

class HistoryPatient:
    def __init__(self, **entries):
        self.id_healing_history: int
        self.patient_id: int
        self.history_neural_network_id: int
        self.history_neutral_network: HistoryNeuralNetwork() = None
        self.patient = None
        self.doctor = None
        self.comment: str
        self.date: str
        self.__dict__.update(entries)

    def get_dict(self):
        h = HistoryPatient()
        if self.history_neutral_network:
            if self.history_neutral_network.annotations:
                for i in self.history_neutral_network.annotations:
                    h.history_neutral_network.annotations.append(Annotations(**i.__dict__).__dict__)
            if self.history_neutral_network.result_predict:
                h.history_neutral_network.result_predict = self.history_neutral_network.result_predict.__dict__
            h.history_neutral_network = h.history_neutral_network.__dict__
        return h.__dict__

    def set_dict(self):
        h = HistoryPatient()
        # print(self.history_neutral_network)
        h_nn = HistoryNeuralNetwork(**self.history_neutral_network)
        print(h_nn.annotations)
        # r = ResultPredict(**self.history_neutral_network.result_predict)
        # a = Annotations(**self.history_neutral_network.annotations)
        # h_nn = HistoryNeuralNetwork(**self.history_neutral_network)
        # h_nn.result_predict = r
        # h_nn.annotations = a
        # h.history_neutral_network = h_nn
        return h


