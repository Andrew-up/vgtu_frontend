from model.result_predict import ResultPredict


class HistoryNeuralNetwork:
    def __init__(self, **entries):
        self.id_history_neural_network = 0
        self.photo_original = None
        self.photo_predict = None
        self.photo_predict_edit_doctor = None
        self.polygon_mask = None
        self.result_predict_id = None
        self.result_predict: ResultPredict.__dict__ = None
        self.healing_history_id = None
        self.area_wound = 0
        self.__dict__.update(entries)
        if self.result_predict is not None:
            self.result_predict = ResultPredict(**self.result_predict)
