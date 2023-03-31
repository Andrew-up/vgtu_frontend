import os.path
import sys

from PySide6.QtWidgets import QWidget, QApplication, QDialog

from definitions import ROOT_DIR
from model.history_training_model import HistoryTrainingModel
from utils.read_xml_file import ReadXmlProject
from view.py.more_info_model_cnn import Ui_Form
from view.user.Update_app_widget import UpdateAppWidget


class MoreInfoModelCnn(QDialog):

    def __init__(self, history_training: HistoryTrainingModel = HistoryTrainingModel(), parent=None):
        super(MoreInfoModelCnn, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.history_train = history_training
        self.ui.date_training.setText(str(history_training.date_train))
        self.ui.status_training.setText(str(history_training.status))
        self.ui.version_model.setText(str(history_training.version))
        self.ui.time_training_model.setText(str(history_training.time_train))
        self.ui.total_epoch.setText(str(history_training.total_epochs))
        self.ui.current_epoch.setText(str(history_training.current_epochs))
        self.ui.pushButton.setEnabled(False)
        self.ui.pushButton.clicked.connect(self.click_download_version)
        if history_training.download and history_training.status == 'completed':
            self.ui.pushButton.setEnabled(True)

    def click_download_version(self):
        xml = ReadXmlProject()
        url_check = xml.get_API() + xml.server_api_check_version
        version_download = f'?version={self.history_train.version}'
        url_download = xml.get_API() + xml.update_cnn_model_api + version_download
        url_installer_exe_path = xml.update_installer_exe_path
        update_dir = os.path.join(ROOT_DIR, 'update_cnn')
        path_end_update = os.path.join(ROOT_DIR, xml.model_cnn_path)

        print(f'end_path: {path_end_update}')

        update = UpdateAppWidget(api_check=url_check,
                                 api_download=url_download,
                                 path_folder_update=update_dir,
                                 path_folder_end=path_end_update,
                                 exe_file_installer_path=url_installer_exe_path,
                                 version_app=self.history_train.version,
                                 filename=self.history_train.name_file,
                                 start_main_exe=False)
        update.exec()


if __name__ == '__main__':
    app = QApplication()
    h = HistoryTrainingModel()
    h.download = True
    h.status = 'completed'
    h.version = '1.0.10'
    window = MoreInfoModelCnn(h)
    window.show()
    sys.exit(app.exec())
