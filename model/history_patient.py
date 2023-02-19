from model.history_neural_network import HistoryNeuralNetwork

class HistoryPatient:
    def __init__(self, **entries):
        self.id_healing_history = 0
        self.patient_id = None
        self.history_neural_network_id = None
        self.history_neutral_network: HistoryNeuralNetwork.__dict__ = None
        self.patient = None
        self.doctor = None
        self.comment = None
        self.date = None
        self.__dict__.update(entries)
        if self.history_neutral_network is not None:
            self.history_neutral_network = HistoryNeuralNetwork(**self.history_neutral_network)

