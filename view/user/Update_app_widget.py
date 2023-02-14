import os
import shutil
import subprocess
import sys
import threading
import time
import zipfile
from threading import Thread

from PySide6.QtCore import QThread, Signal, Slot
from PySide6.QtWidgets import QWidget, QApplication, QMessageBox, QDialog
from view.py.update_app import Ui_Form
import xml.etree.ElementTree as ET
import requests
from definitions import ROOT_DIR
import install_update

class app_class(object):
    server_addr: str = None
    server_port = None
    version = None
    new_version = None
    root_dir = None
    exe_file_main = None
    update_dir = None
    update_api = None
    check_version_api = None

    def get_root_API(self):
        return f'http://{self.server_addr}:{self.server_port}/'

    def get_check_version_API(self):
        return f'{self.get_root_API()}{self.check_version_api}'
        pass

    def download_version_API(self):
        return f'{self.get_root_API()}{self.update_api}'
        pass

    def get_update_dir(self):
        return f'{self.root_dir}/{self.update_dir}'

    def get_root_dir(self):
        return self.root_dir

    def get_xml_dir(self):
        return f'{self.root_dir}/project.xml'

class UpdateApp(QThread):
    signal_download_ok = Signal()
    signal_download_error = Signal(str)
    value_progress = Signal(int)

    def __init__(self, parent=None):
        super(UpdateApp, self).__init__(parent)
        self.setting_app = None
        self.setting_app: app_class()


    def set_setting_app(self, setting: app_class()):
        self.setting_app = setting

    def get_setting_app(self) -> app_class:
        return self.setting_app


    def run(self):
        print("======== ЗАГРУЖАЮ ОБНОВЛЕНИЕ =======")
        addr_upd = self.get_setting_app().download_version_API()
        print(self.get_setting_app().update_dir)
        if addr_upd is not None:
            response = requests.get(addr_upd, stream=True)
            if response.status_code != 200:
                print(f'status: {response.status_code}')
                self.signal_download_error.emit(response.text)
            if response.status_code == 200:
                print('status 200')
                if os.path.exists(self.get_setting_app().update_dir):
                    print(f'Папка {self.get_setting_app().update_dir} есть')
                else:
                    try:
                        os.makedirs(f'{self.get_setting_app().update_dir}')
                    except OSError as error:
                        print(f"Directory '{self.get_setting_app().update_dir}' can not be created")
                with open(f'{self.get_setting_app().update_dir}/update.zip', 'wb') as out_file:
                    total_size = int(response.headers.get('Content-Length'))
                    chunk_size = int(round(total_size)/100)
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
                    self.value_progress.emit(100)
                    self.signal_download_ok.emit()
        else:
            msg = QMessageBox()
            msg.setText('API NOT FOUND')
            msg.exec()


class UpdateAppWidget(QDialog):

    def __init__(self, parent=None):
        super(UpdateAppWidget, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.check_version)

        # Установить прогресс бар на 0 %
        self.ui.progressBar.setValue(0)
        # ---------------

        # Создать класс app_class
        self.app_setting = app_class()
        # Добавить ROOT DIR в app class
        self.init_root_dit()
        # ---------------
        # Прочитать все поля из xml
        self.read_xml()
        # ---------------

        # Поток для загрузки файла
        self.update_class = UpdateApp(self)
        self.update_class.set_setting_app(self.app_setting)
        self.update_class.signal_download_ok.connect(self.on_download_ok)
        self.update_class.signal_download_error.connect(self.on_download_error)
        self.update_class.value_progress.connect(self.set_value_progress)
        # ---------------

        self.ui.pushButton_2.setEnabled(False)
        self.ui.pushButton_2.clicked.connect(self.install_update_start_exe)

    @Slot(int)
    def set_value_progress(self, progress: int):
        # print(progress)
        self.ui.progressBar.setValue(progress)

    @Slot()
    def on_download_ok(self):
        self.unpack_zip_file()
        # self.ui.pushButton_2.setEnabled(True)

    @Slot(str)
    def on_download_error(self, str):
        msg = QMessageBox()
        msg.setText(f'{str}')
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.exec()

    def install_update_start_exe(self):
        # w = Worker(path_temp=self.app_setting.get_update_dir(), path_target=self.app_setting.get_root_dir())
        # str = f'{self.app_setting.get_root_dir()}/dist/install_update.exe "{self.app_setting.get_update_dir()}" "{self.app_setting.get_root_dir()}"'
        # s = Worker("123", "123")
        # s.daemon = True
        # s.start()
        s = threading.Thread(target=install_update.startappppps, daemon=True)
        s.start()
        time.sleep(2)
        print('122222222')
        # time.sleep(2)
        # time.sleep(3)
        app.quit()

    def check_version(self):
        adr = self.app_setting.get_check_version_API()
        print(adr)
        r = requests.get(adr)
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
                self.ui.label.setText(f"Идет загрузка новой версии приложения {self.app_setting.new_version}")
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
        et = ET.parse('../../project.xml')
        app_n = et.find('app')
        version_n = app_n.find('version')
        version_n.text = self.app_setting.new_version
        et.write('project.xml')

    def read_xml(self):
        print(self.app_setting.get_xml_dir())
        if os.path.exists(self.app_setting.get_xml_dir()):
            root_node = ET.parse(self.app_setting.get_xml_dir()).getroot()
            app = root_node.find('app')
            self.app_setting.update_dir = app.find('temp_update').text
            self.app_setting.exe_file_main = app.find('exe_file_main').text
            self.app_setting.version = app.find('version').text

            server = root_node.find('server')
            self.app_setting.server_addr = server.find('addr').text
            self.app_setting.server_port = server.find('port').text
            self.app_setting.update_api = server.find('update_api').text
            self.app_setting.check_version_api = server.find('check_version_api').text

        else:
            print('не найден project.xml')

    def init_root_dit(self):
        # ROOT_DIR = ''  # This is your Project Root
        # if getattr(sys, 'frozen', False):
        #     ROOT_DIR = os.path.dirname(sys.executable)
        # elif __file__:
        #     ROOT_DIR = os.path.dirname(__file__)
        self.app_setting.root_dir = ROOT_DIR

    def unpack_zip_file(self):
        self.ui.label.setText('Идет распаковка файлов')
        catalog_unpack_zip = self.app_setting.update_dir
        zip_file_temp = f'{catalog_unpack_zip}/update.zip'
        try:
            with zipfile.ZipFile(zip_file_temp, 'r') as zip_file:
                try:
                    print('пытаюсь распаковать')
                    zip_file.extractall(f'{catalog_unpack_zip}')
                    print('распаковка успешна')
                except zipfile.BadZipfile as e:
                    print('распаковка ошибка')
                    print(e)
            try:
                print(f'Удаляю {zip_file_temp}')
                os.remove(zip_file_temp)
            except OSError as error:
                print(f'remove {zip_file_temp} error: {error}')

        except BaseException as e:
            msg = QMessageBox()
            msg.setWindowTitle('Ошибка!')
            msg.setIcon(QMessageBox.Icon.Critical)
            msg.setText(e)
            msg.exec()
        self.ui.pushButton_2.setEnabled(True)
        self.ui.label.setText('Распаковка окончена. \n Для установки обновлений нажмите на кнопку \n "Установить обновления"')


# class Worker(Thread):
#     def __init__(self, parent=None):
#         super(Worker, self).__init__(parent)
#         self.API = None
#
#     def run(self):
#         subprocess.run('Update_app_widget.exe')
#         count = 1
#         print('--------------')
#         while count < 10:
#             print(count)
#             time.sleep(1)
#             count += 1


if __name__ == '__main__':
    # upd = Worker()
    # upd.daemon = True
    # upd.start()
    # sys.exit(app.exec())
    app = QApplication()
    window = UpdateAppWidget()
    window.show()
    sys.exit(app.exec())