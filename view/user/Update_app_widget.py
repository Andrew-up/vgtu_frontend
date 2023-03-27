import os
import shutil
import subprocess
import sys
import time
import xml.etree.ElementTree as ET
import zipfile

import requests
from PySide6.QtCore import QThread, Signal, Slot
from PySide6.QtWidgets import QApplication, QMessageBox, QDialog

from definitions import ROOT_DIR
from view.py.update_app import Ui_Form
from urllib.parse import urlparse
from utils.read_xml_file import ReadXmlProject


class UpdateApp(QThread):
    signal_download_ok = Signal()
    signal_download_error = Signal(str)
    value_progress = Signal(int)

    def __init__(self, parent=None):
        super(UpdateApp, self).__init__(parent)
        self._api_download = None
        self._dir_files = None

    def set_api_download(self, API: str):
        self._api_download = API

    def get_api_download(self):
        return self._api_download

    def set_dir(self, dir_file: str):
        self._dir_files = dir_file

    def get_dir(self):
        return self._dir_files

    def run(self):
        if self.get_dir() is None:
            print('111111111')
            self.signal_download_error.emit('директория не задана')
            return 0
        print(self.get_dir())
        if self.get_api_download() is None:
            print('22222222')
            self.signal_download_error.emit('api не задан')
            return 0
        print(self.get_api_download())
        addr_upd = self.get_api_download()
        print("======== ЗАГРУЖАЮ ОБНОВЛЕНИЕ =======")
        response = requests.get(addr_upd, stream=True)
        if response.status_code != 200:
            print(f'status: {response.status_code}')
            self.signal_download_error.emit(response.text)
        if response.status_code == 200:
            print('status 200')
            if os.path.exists(self.get_dir()):
                print(f'Папка {self.get_dir()} есть')
            else:
                try:
                    os.makedirs(f'{self.get_dir()}')
                except OSError as error:
                    print(f"Directory '{self.get_dir()}' can not be created")
            with open(f'{self.get_dir()}/update.zip', 'wb') as out_file:
                total_size = int(response.headers.get('Content-Length'))
                chunk_size = int(round(total_size) / 100)
                print(total_size)
                for i, chunk in enumerate(response.iter_content(chunk_size=chunk_size)):
                    # calculate current percentage
                    c = i * chunk_size / total_size * 100
                    progress = round(c)
                    self.value_progress.emit(progress)
                    out_file.write(chunk)
                shutil.copyfileobj(response.raw, out_file)
                time.sleep(0.2)
                self.value_progress.emit(100)
                self.signal_download_ok.emit()


class UpdateAppWidget(QDialog):
    close_app = Signal()

    def __init__(self, parent=None):
        super(UpdateAppWidget, self).__init__(parent)
        self.root = parent
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.check_version)

        # Установить прогресс бар на 0 %
        self.ui.progressBar.setValue(0)
        # ---------------

        # Поток для загрузки файла
        self.update_class = UpdateApp(self)
        self.update_class.signal_download_ok.connect(self.on_download_ok)
        self.update_class.signal_download_error.connect(self.message_error_show)
        self.update_class.value_progress.connect(self.set_value_progress)
        # ---------------
        # self.ui.pushButton_2.setEnabled(False)
        self.ui.pushButton_2.clicked.connect(self.install_update_start_exe)

        self._api_check = None
        self._api_download = None
        self._path_folder_update = None
        self._path_folder_end = None
        self._exe_file_installer_path = None
        self._version = None
        self._start_main_exe = False


    def set_param(self, api_check,
                  api_download,
                  path_folder_update,
                  path_folder_end,
                  exe_file_installer_path,
                  version_app,
                  start_main_exe=False):
        self._api_check = api_check
        self._api_download = api_download
        self._path_folder_update = path_folder_update
        self._path_folder_end = path_folder_end
        self._exe_file_installer_path = exe_file_installer_path
        self._version = version_app
        self._start_main_exe = start_main_exe

    @property
    def start_main_exe(self):
        return self._start_main_exe

    @property
    def api_check(self):
        return self._api_check

    @property
    def api_download(self):
        return self._api_download

    @property
    def path_folder_update(self):
        return self._path_folder_update

    @property
    def path_folder_end(self):
        return self._path_folder_end

    @property
    def exe_file_installer_path(self):
        return self._exe_file_installer_path

    @property
    def version(self):
        return self._version

    @Slot(int)
    def set_value_progress(self, progress: int):
        # print(progress)
        self.ui.progressBar.setValue(progress)

    @Slot()
    def on_download_ok(self):
        self.ui.label.setText('Загрузка окончена.'
                              ' \n Для установки обновлений нажмите на кнопку'
                              ' \n "Установить обновления"')
        self.ui.pushButton_2.setEnabled(True)

    @Slot(str)
    def message_error_show(self, message):
        msg = QMessageBox()
        msg.setText(f'{message}')
        self.ui.label.setText(f"Ошибка: {message}")
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.exec()

    def install_update_start_exe(self):
        msg = QMessageBox()
        msg.setWindowTitle('Установка обновлений')
        print(self.start_main_exe)

        if self.start_main_exe:
            msg.setText('Для установки обновлений требуется перезапуск приложения\n'
                        'Перезапустить приложение?')
        else:
            msg.setText('Подтвердите запуск подпрограммы для распаковки файлов')

        msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)
        res = msg.exec()
        if res == QMessageBox.StandardButton.Yes:
            if not os.path.exists(self.exe_file_installer_path):
                self.message_error_show(
                    f"Ошибка, не найден файл для установки обновлений:\n {self.exe_file_installer_path} \n"
                    f"Проверьте project.xml")
                return 0
            exe_installer = self.exe_file_installer_path
            update_dir = self.path_folder_update
            send_download_files_to_dir = self.path_folder_end
            str = f'{exe_installer} "{update_dir}" "{send_download_files_to_dir}" "{self.start_main_exe}"'
            subprocess.Popen(str)
            if self.start_main_exe:
                if self.root is None:
                    print(self.root)
                    app.quit()
                self.close_app.emit()
        else:
            print('Отмена обновлений')

    def url_validator(self, x):
        try:
            result = urlparse(x)
            return all([result.scheme, result.netloc])
        except:
            return False

    def check_version(self):
        adr = self.api_check
        if not self.url_validator(adr):
            self.message_error_show(f"Адрес {adr} не валидный")
            return 0
        r = requests.get(adr)
        print(adr)
        if r.status_code != 200:
            self.message_error_show('Сервер вернул код отличный от 200\n'
                                    f'{r.text}')

        if r.text > self.version and r.status_code == 200:
            msg = QMessageBox()
            msg.setWindowTitle('Проверка обновлений')
            msg.setText(f'Ваша версия: {self.version}\n'
                        f'Доступна версия: {r.text}\n'
                        f'Скачать новую версию?\n')
            msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)
            res = msg.exec()
            if res == QMessageBox.StandardButton.Yes:
                if not self.url_validator(self.api_download):
                    self.message_error_show(f"Адрес для загрузки: \" {self.api_download} \" не валидный")
                    return 0
                self.update_class.set_dir(os.path.join(ROOT_DIR, self.path_folder_update))
                self.update_class.set_api_download(self.api_download)
                self.update_class.start()
                self.ui.label.setText(f"Идет загрузка новой версии приложения {r.text}")
                print('Скачиваю новую версию')
            if res == QMessageBox.StandardButton.Cancel:
                print('Отмена скачивания')
        else:
            msg = QMessageBox()
            msg.setWindowTitle('Проверка обновлений')
            msg.setText('Обновлений нет.')
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.exec()


if __name__ == '__main__':
    # upd = Worker()
    # upd.daemon = True
    # upd.start()
    # sys.exit(app.exec())
    xml = ReadXmlProject()
    url_check = xml.get_API() + xml.server_api_check_version
    version_download = '?version=1.0.9'
    url_download = xml.get_API() + xml.update_cnn_model_api+version_download

    url_installer_exe_path = xml.update_installer_exe_path
    update_dir = ROOT_DIR + '/333'
    path_end_update = ROOT_DIR + '/4444'
    version = xml.model_cnn_version
    app = QApplication()
    window = UpdateAppWidget()
    window.set_param(api_check=url_check,
                     api_download=url_download,
                     path_folder_update=update_dir,
                     path_folder_end=path_end_update,
                     exe_file_installer_path=url_installer_exe_path,
                     version_app=version,
                     start_main_exe=False)
    window.show()
    sys.exit(app.exec())
