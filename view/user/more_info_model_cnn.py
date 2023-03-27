import sys

from PySide6.QtWidgets import QWidget, QApplication, QDialog
from model.history_training_model import HistoryTrainingModel
from view.py.more_info_model_cnn import Ui_Form


class MoreInfoModelCnn(QDialog):

    def __init__(self, history_training: HistoryTrainingModel = HistoryTrainingModel(), parent=None):
        super(MoreInfoModelCnn, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.date_training.setText(str(history_training.date_train))
        self.ui.status_training.setText(str(history_training.status))
        self.ui.version_model.setText(str(history_training.version))
        self.ui.time_training_model.setText(str(history_training.time_train))
        self.ui.total_epoch.setText(str(history_training.total_epochs))
        self.ui.current_epoch.setText(str(history_training.current_epochs))
        self.ui.pushButton.setEnabled(False)
        if history_training.download and history_training.status == 'completed':
            self.ui.pushButton.setEnabled(True)

if __name__ == '__main__':
    app = QApplication()
    window = MoreInfoModelCnn()
    window.show()
    sys.exit(app.exec())
