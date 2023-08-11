from model.result_predict import ResultPredict

class Annotations:
    def __init__(self, **entries):
        self.id_annotations: int = int()
        self.area: float = float()
        self.bbox: list[float] = []
        self.segmentation: list[float] = []
        self.history_nn_id: int = int()
        self.category_id: int = int()
        self.result_predict: ResultPredict = ResultPredict()
        self.__dict__.update(entries)

