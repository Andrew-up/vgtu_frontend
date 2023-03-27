import sys

from PySide6.QtWidgets import QWidget, QApplication
from model.history_training_model import HistoryTrainingModel
from view.py.info_model_cnn_item import Ui_Form
from view.user.more_info_model_cnn import MoreInfoModelCnn


class ItemInfoModelCNN(QWidget):

    def __init__(self, history_training: HistoryTrainingModel = HistoryTrainingModel(), parent=None):
        super(ItemInfoModelCNN, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.history_training = history_training
        self.ui.label.setText('Версия: '+str(self.history_training.version))
        self.ui.pushButton.clicked.connect(self.open_more_info_model)

    def open_more_info_model(self):
        dlg = MoreInfoModelCnn(self.history_training)
        dlg.exec()



if __name__ == '__main__':
    app = QApplication()
    window = ItemInfoModelCNN()
    window.show()
    sys.exit(app.exec())
