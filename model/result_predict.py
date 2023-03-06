class ResultPredict:
    def __init__(self, **entries):
        self.id_category: int = 0
        self.name_category_eng: str = str()
        self.name_category_ru: str = str()
        self.color: tuple = tuple()
        self.__dict__.update(entries)
