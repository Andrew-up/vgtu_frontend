class HistoryTrainingModel(object):

    def __init__(self, **entries):
        self.id = None
        self.version = None
        self.accuracy = None
        self.name_file = None
        self.date_train = None
        self.quality_dataset = None
        self.quality_train_dataset = None
        self.quality_valid_dataset = None
        self.current_epochs = None
        self.total_epochs = None
        self.time_train = None
        self.num_classes = None
        self.input_size = None
        self.output_size = None
        self.status = None
        self.download = False
        self.__dict__.update(entries)

