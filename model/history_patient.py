from model.history_neural_network import HistoryNeuralNetwork
from model.Annotations import Annotations
from model.result_predict import  ResultPredict

class HistoryPatient:
    def __init__(self, **entries):
        self.id_healing_history: int
        self.patient_id: int = int()
        self.history_neural_network_id: int
        self.history_neutral_network: HistoryNeuralNetwork = HistoryNeuralNetwork()
        self.patient = None
        self.doctor = None
        self.comment: str = str()
        self.date: str = str()
        self.__dict__.update(entries)

    def get_dict(self):
        h = HistoryPatient()
        h.history_neutral_network = HistoryNeuralNetwork()
        if self.history_neutral_network:

            h.patient_id = self.patient_id

            h.history_neutral_network.photo_original = self.history_neutral_network.photo_original
            h.history_neutral_network.photo_predict = self.history_neutral_network.photo_predict
            h.history_neutral_network.photo_predict_edit_doctor = self.history_neutral_network.photo_predict_edit_doctor
            h.date = self.date
            h.comment = self.comment

            if self.history_neutral_network.annotations:
                print(len(self.history_neutral_network.annotations))
                h.history_neutral_network.annotations = []
                for i in self.history_neutral_network.annotations:
                    print('=====================')
                    if i.id_annotations is None:
                        i.id_annotations = 0
                    else:
                        i.id_annotations += 1
                    print(i.result_predict)
                    if i.result_predict:
                        i.result_predict = i.result_predict.__dict__
                    print(i.area)

                    h.history_neutral_network.annotations.append(i.__dict__)
            h.history_neutral_network = h.history_neutral_network.__dict__
        return h

    def set_dict(self):
        h = HistoryPatient()
        if self:
            if self.history_neutral_network:
                h_nn = HistoryNeuralNetwork(**self.history_neutral_network)
                list_a = []
                for i in h_nn.annotations:
                    a = Annotations(**i)
                    if a.result_predict:
                        a.result_predict = ResultPredict(**a.result_predict)
                    list_a.append(a)
                h_nn.annotations = list_a
                h.history_neutral_network = h_nn
                h.date = self.date
                h.comment = self.comment

        return h


