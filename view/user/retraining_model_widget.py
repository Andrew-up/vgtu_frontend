import sys

from PySide6.QtWidgets import QWidget, QApplication, QDialog
from model.history_training_model import HistoryTrainingModel
from view.py.Retraining_model import Ui_Form
from controller.model_cnn_controller import get_annotation_json, get_last_history_training, send_retraining_model

class RetrainingModelWidget(QDialog):

    def __init__(self, history_training: HistoryTrainingModel = HistoryTrainingModel(), parent=None):
        super(RetrainingModelWidget, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.history_training = history_training
        self.last_history_training = get_last_history_training()

        self.inizializator()
        self.ui.pushButton.clicked.connect(self.on_retraining_button)

    def inizializator(self):
        self.ui.model_training_false.setVisible(False)
        self.ui.widget.setVisible(False)
        if self.last_history_training['status'] == 'completed':
            ann_json = get_annotation_json()
            self.ui.widget.setVisible(True)
            self.ui.total_annotation_label.setText(str(len(ann_json['annotations'])))
            self.ui.total_category_label.setText(str(len(ann_json['categories'])))
            self.ui.total_images_label.setText(str(len(ann_json['images'])))
            self.ui.pushButton.setEnabled(True)
        else:
            self.ui.model_training_false.setVisible(True)


    def on_retraining_button(self):
        send_retraining_model()
        self.last_history_training = get_last_history_training()
        self.inizializator()

    def open_more_info_model(self):
        dlg = RetrainingModelWidget(self.history_training)
        dlg.exec()



if __name__ == '__main__':
    app = QApplication()
    window = RetrainingModelWidget()
    window.show()
    sys.exit(app.exec())
