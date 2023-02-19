class ResultPredict:
    def __init__(self, **entries):
        self.id_category = 0
        self.name_category_eng = None
        self.name_category_ru = None
        self.history_neural_network = None
        self.__dict__.update(entries)
