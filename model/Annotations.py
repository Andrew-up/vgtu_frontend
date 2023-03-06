class Annotations:
    def __init__(self, **entries):
        self.id_annotations: int
        self.area: float
        self.bbox: str
        self.segmentation: str
        self.history_nn_id: int
        self.category_id: int
        self.__dict__.update(entries)

