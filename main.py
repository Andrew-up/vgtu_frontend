import time

timer = time.time()
import os
import sys
import urllib.parse

import requests
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget

from definitions import ROOT_DIR
from service.slotsService import SlotsMainMenu
from utils.read_xml_file import ReadXmlProject
from view.py.mainwindow import Ui_MainWindow
import threading
from view.user.info_model_cnn_widget import InfoModelCNNWidget



print(f"time: {time.time() - timer}")


class MainWindow(QMainWindow):
    this_class_slot = SlotsMainMenu()

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        print('1111111111111111')
        self.r = ReadXmlProject()
        self.ui.widget_server_connect.setVisible(False)
        self.ui.textEdit.setReadOnly(True)
        self.this_class_slot.open_start_view.connect(self.open_start_view)
        self.this_class_slot.set_widget_main_menu.connect(self.set_widget_root_stacket_widget)
        self.ui.pushButton.clicked.connect(self.update_app)
        self.ui.logo_company_main.setStyleSheet('background-color: white')
        self.ui.logo_company_main.setText('ROBOT HELPER')
        self.ui.update_cnn_button.clicked.connect(self.open_cnn_dialog)
        self.ui.reload_connect_server.clicked.connect(self.check_status_server)
        self.check_status_server()
        thread = threading.Thread(target=self.load_app)
        thread.start()

    def check_status_server(self) -> bool:
        print('обновить')
        url_check = urllib.parse.urljoin(self.r.get_API(), 'api/app/status/')
        try:
            r = requests.get(url_check)
            if r.json()['status'] == "ok":
                print(r.json())
                self.ui.widget_server_connect.setVisible(False)
                self.view_patient()
                # return True
            else:
                self.ui.widget_server_connect.setVisible(True)
                self.ui.textEdit.setText(r.text)
                return False
        except requests.exceptions.RequestException as e:  # This is the correct syntax
            self.ui.widget_server_connect.setVisible(True)
            self.ui.textEdit.setText(str(e))
            return False

    def open_cnn_dialog(self):
        dlg = InfoModelCNNWidget()
        dlg.exec()

    def load_app(self):
        print('Идет загрузка приложения...')
        from view.user.card_patient_widget import CardPatient
        from view.user.history_patient_widget import HistoryPatient
        from view.user.wound_treatment_widget import WoundHealingPatient
        print('загрузка завершена')
        self.ui.label.setText('Загрузка завершена')
        time.sleep(5)
        self.ui.widget_2.setVisible(False)

    def view_patient(self):
        from view.user.list_patient_widget import ListPatient
        list_patient = ListPatient(self)
        list_patient.set_main_menu_slots(self.this_class_slot)
        list_patient.get_all_patient()
        self.this_class_slot.set_widget_main_menu.emit(list_patient)

    def close_app(self):
        app.quit()
        sys.exit(app.exec())

    @Slot()
    def update_app(self):
        from view.user.Update_app_widget import UpdateAppWidget

        url_check = self.r.get_API() + self.r.server_api_check_version
        url_download = self.r.get_API() + self.r.server_api_update
        url_installer_exe_path = self.r.update_installer_exe_path
        update_dir = self.r.app_update_folder
        path_end_update = os.path.join(ROOT_DIR)
        version = self.r.app_version
        print(f'end_path: {path_end_update}')

        dlg = UpdateAppWidget(api_check=url_check,
                              api_download=url_download,
                              path_folder_update=update_dir,
                              path_folder_end=path_end_update,
                              exe_file_installer_path=url_installer_exe_path,
                              version_app=version,
                              start_main_exe=True)
        dlg.close_app.connect(self.close_app)
        dlg.exec()

    @Slot()
    def open_start_view(self):
        self.view_patient()
        print('открыть стартовое меню')

    @Slot(QWidget)
    def set_widget_root_stacket_widget(self, widget: QWidget):
        print('Сработал сигнал set_widget_root_stacket_widget')
        self.clear_stacked_widget()
        self.ui.stacked_widget_main.addWidget(widget)
        self.ui.stacked_widget_main.setCurrentWidget(widget)

    def getCountStacketWidget(self) -> int:
        count = self.ui.stacked_widget_main.count()
        print(f'stacked widget main menu count == {count}')
        return count

    def clear_stacked_widget(self):
        if self.getCountStacketWidget() > 10:
            pages = self.ui.stacked_widget_main.count()
            for i in range(pages):
                widget = self.ui.stacked_widget_main.widget(0)
                self.ui.stacked_widget_main.removeWidget(widget)
            print('сработала очистка stacked widget')
        else:
            print('Еще рано очищать stacked widget')


if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec())
    except BaseException as e:
        print(e)
