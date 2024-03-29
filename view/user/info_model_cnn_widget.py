import sys

from PySide6.QtWidgets import QWidget, QApplication, QDialog

from model.history_patient import HistoryPatient
from view.py.info_model_cnn import Ui_Form
from model.history_training_model import HistoryTrainingModel
from controller.model_cnn_controller import get_history_training_model
from view.user.info_model_cnn_item import ItemInfoModelCNN
from view.user.retraining_model_widget import RetrainingModelWidget

class InfoModelCNNWidget(QDialog):

    def __init__(self, parent=None):
        super(InfoModelCNNWidget, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.history_training_list = []
        self.get_all_history()
        self.ui.pushButton.clicked.connect(self.open_dialog_retraining_model)

    def open_dialog_retraining_model(self):
        r = RetrainingModelWidget()
        r.exec()
        self.get_all_history()


    def get_all_history(self):
        self.history_training_list = get_history_training_model()
        for i in reversed(range(self.ui.verticalLayout_3.count())):
            self.ui.verticalLayout_3.itemAt(i).widget().setParent(None)
        self.add_item_from_list_history(self.history_training_list)

    def add_item_from_list_history(self, list_history):

        for i in list_history:

            w = ItemInfoModelCNN(i)
            w.signal111.connect(self.get_all_history)
            self.ui.verticalLayout_3.addWidget(w)




if __name__ == '__main__':
    app = QApplication()
    window = InfoModelCNNWidget()
    window.show()
    sys.exit(app.exec())
