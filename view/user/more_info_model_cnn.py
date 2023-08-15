import os.path
import sys

from PySide6.QtWidgets import QApplication, QDialog, QMessageBox

from controller.model_cnn_controller import delete_model_by_id, get_model_by_id
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
        self.ui.pushButton.setEnabled(False)
        self.history_train = history_training
        self.update_self_widget(self.history_train)
        self.ui.pushButton.clicked.connect(self.click_download_version)
        self.ui.pushButton_2.clicked.connect(self.delete_model_by_id)
        self.ui.pushButton_3.clicked.connect(self.update_model)

    def update_model(self):
        # print(get_model_by_id(self.history_train.id))
        upd = HistoryTrainingModel(**get_model_by_id(self.history_train.id))
        self.update_self_widget(upd)

    def update_self_widget(self, history: HistoryTrainingModel):
        self.ui.date_training.setText(str(history.date_train))
        self.ui.status_training.setText(str(history.status))
        self.ui.version_model.setText(str(history.version))
        self.ui.time_training_model.setText(str(history.time_train))
        self.ui.total_epoch.setText(str(history.total_epochs))
        self.ui.current_epoch.setText(str(history.current_epochs))
        print(history.download)
        print(history.status)
        if history.download and history.status == 'completed':
            self.ui.pushButton.setEnabled(True)

    def delete_model_by_id(self):
        if self.history_train.id:
            print(self.history_train.id)

            msg = QMessageBox()
            msg.setInformativeText(f"Удалить CNN{self.history_train.version}\n"
                                   f"id: {self.history_train.id} ? \n"
                                   f"Удаление отменить невозможно.")
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setWindowTitle("Удаление истории модели")
            msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)
            res = msg.exec()
            if res == QMessageBox.StandardButton.Yes:
                print('Удаляем')
                delete_model_by_id(self.history_train.id)
                self.close()
            if res == QMessageBox.StandardButton.Cancel:
                print('Отмена удаления')

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
    h.id = "1"
    window = MoreInfoModelCnn(h)
    window.show()
    sys.exit(app.exec())
