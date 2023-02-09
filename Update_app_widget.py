import os
import shutil
import subprocess
import sys
import time
import zipfile

from PySide6.QtCore import QThread, Signal, Slot
from PySide6.QtWidgets import QWidget, QApplication, QMessageBox
from view.py.update_app import Ui_Form
import xml.etree.ElementTree as ET
import requests


class UpdateApp(QThread):
    signal_download_ok = Signal()
    signal_download_error = Signal(str)
    value_progress = Signal(int)

    def __init__(self, parent=None):
        super(UpdateApp, self).__init__(parent)
        self.API = None

    def run(self):
        print("======== ЗАГРУЖАЮ ОБНОВЛЕНИЕ =======")
        if self.API is not None:
            print(self.API)
            response = requests.get(self.API, stream=True)
            if response.status_code != 200:
                print(f'status: {response.status_code}')
                self.signal_download_error.emit(response.text)

            if response.status_code == 200:
                print('status 200')
                with open('update.zip', 'wb') as out_file:
                    total_size = int(response.headers.get('Content-Length'))
                    chunk_size = 4096
                    print(total_size)
                    # print(response.iter_content(chunk_size=chunk_size))
                    for i, chunk in enumerate(response.iter_content(chunk_size=chunk_size)):
                        # calculate current percentage
                        c = i * chunk_size / total_size * 100
                        progress = round(c)
                        self.value_progress.emit(progress)
                        out_file.write(chunk)
                    shutil.copyfileobj(response.raw, out_file)
                    time.sleep(0.2)
                    self.signal_download_ok.emit()
        else:
            msg = QMessageBox()
            msg.setText('API NOT FOUND')
            msg.exec()


class app_class(object):
    server_addr: str = None
    server_port = None
    version = None
    new_version = None

class UpdateAppWidget(QWidget):

    def __init__(self, parent=None):
        super(UpdateAppWidget, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.app_setting = app_class()

        self.ui.pushButton_2.clicked.connect(self.install_update)
        self.ui.pushButton.clicked.connect(self.check_version)
        self.update_class = UpdateApp(self)
        self.update_class.signal_download_ok.connect(self.on_download_ok)
        self.update_class.signal_download_error.connect(self.on_download_error)
        self.update_class.value_progress.connect(self.set_value_progress)
        self.ui.progressBar.setValue(0)
        self.ROOT_DIR = None
        self.read_xml()
        self.ui.pushButton_2.setEnabled(False)



    @Slot(int)
    def set_value_progress(self, progress: int):
        print(progress)
        self.ui.progressBar.setValue(progress)

    @Slot()
    def on_download_ok(self):
        self.ui.pushButton_2.setEnabled(True)

    @Slot(str)
    def on_download_error(self, str):
        msg = QMessageBox()
        msg.setText(f'{str}')
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.exec()


    def check_version(self):
        print(self.app_setting.version)
        print(self.app_setting.server_port)
        addr_server = f'http://{self.app_setting.server_addr}:{self.app_setting.server_port}/app/version'
        r = requests.get(addr_server)
        if r.status_code != 200:
            msg = QMessageBox()
            msg.setText('Сервер вернул код отличный от 200')
            msg.exec()
        print(r.text)
        if r.text > self.app_setting.version and r.status_code == 200:
            self.app_setting.new_version = r.text
            msg = QMessageBox()
            msg.setWindowTitle('Проверка обновлений')
            msg.setText(f'Ваша версия приложения: {self.app_setting.version}\n'
                        f'Доступна версия: {r.text}\n'
                        f'Скачать новую версию?\n')
            msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)
            res = msg.exec()
            if res == QMessageBox.StandardButton.Yes:
                self.update_class.start()
                print('Скачиваю новую версию')
            if res == QMessageBox.StandardButton.Cancel:
                print('Отмена скачивания')
        else:
            msg = QMessageBox()
            msg.setWindowTitle('Проверка обновлений')
            msg.setText('Обновлений нет.')
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.exec()


    def update_version_xml(self):
        et = ET.parse('project.xml')
        app_n = et.find('app')
        version_n = app_n.find('version')
        version_n.text = self.app_setting.new_version
        et.write('project.xml')


    def read_xml(self):
        root_node = ET.parse('project.xml').getroot()
        app = root_node.find('app')
        version = app.find('version')
        update_api = app.find('update_api')
        print(update_api.text)
        server = root_node.find('server')
        server_addr = server.find('addr')
        server_port = server.find('port')
        self.app_setting.server_addr = server_addr.text
        self.app_setting.server_port = server_port.text
        self.app_setting.version = version.text
        self.update_class.API = f'http://{server_addr.text}:{server_port.text}/{update_api.text}'


    def install_update(self):
        ROOT_DIR = ''  # This is your Project Root
        if getattr(sys, 'frozen', False):
            ROOT_DIR = os.path.dirname(sys.executable)
        elif __file__:
            ROOT_DIR = os.path.dirname(__file__)
        ZIP_FILE_UPDATE = os.path.join(ROOT_DIR, "update.zip")
        EXE = os.path.join(ROOT_DIR, "main.exe")
        try:
            with zipfile.ZipFile(ZIP_FILE_UPDATE, 'r') as zip_file:
                try:
                    print('пытаюсь распаковать')
                    zip_file.extractall(f'{ROOT_DIR}')
                    print('распаковка успешна')
                except zipfile.BadZipfile as e:
                    print('распаковка ошибка')
                    print(e)
            try:
                subprocess.check_call(EXE)
                self.update_version_xml()
                # app.quit()

            except Exception as f:
                msg = QMessageBox()
                msg.setWindowTitle('Ошибка!')
                msg.setIcon(QMessageBox.Icon.Critical)
                msg.setText(str(f))
                msg.exec()

        except BaseException as e:
            msg = QMessageBox()
            msg.setWindowTitle('Ошибка!')
            msg.setIcon(QMessageBox.Icon.Critical)
            msg.setText(e)
            msg.exec()


if __name__ == '__main__':
    app = QApplication()
    window = UpdateAppWidget()
    window.show()
    sys.exit(app.exec())
