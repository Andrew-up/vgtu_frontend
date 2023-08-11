import sys

from definitions import ROOT_DIR
import os.path
import xml.etree.ElementTree as ET


class ReadXmlProject(object):

    def __init__(self):
        self.file_path = os.path.join(ROOT_DIR, 'project.xml')
        self._app_version = None
        self._app_exe_file_main = None
        self._app_update_folder = None
        self._server_addr = None
        self._server_port = None
        self._server_api_update = None
        self._server_api_check_version = None
        self._coefficient_k = None
        self._model_cnn_path = None
        self._model_cnn_name = None
        self._update_installer_exe_path = None
        self._file_name_archive = None
        self._exe_file_main = None
        self._model_cnn_version = None
        self._update_cnn_model_api = None
        self._init_variable()

    def update_file_name_model_cnn(self, new_file_name: str):
        root_node = ET.parse(self.file_path)
        app = root_node.getroot().find('app')
        text = app.find('model_cnn_name')
        text.text = new_file_name
        root_node.write(self.file_path)
    def update_file_version_cnn_model(self, new_file_name: str):
        root_node = ET.parse(self.file_path)
        app = root_node.getroot().find('app')
        text = app.find('model_cnn_version')
        text.text = new_file_name
        root_node.write(self.file_path)

    def _init_variable(self):
        if os.path.exists(self.file_path):
            root_node = ET.parse(self.file_path).getroot()
            app = root_node.find('app')
            self._app_update_folder = app.find('temp_update').text
            self._app_version = app.find('version').text
            self._coefficient_k = app.find('coefficient_k').text
            self._model_cnn_path = app.find('model_cnn_path').text
            self._model_cnn_name = app.find('model_cnn_name').text
            self._update_installer_exe_path = app.find('update_installer_exe_path').text
            self._exe_file_main = app.find('exe_file_main').text
            self._file_name_archive = app.find('file_name_archive').text
            self._model_cnn_version = app.find('model_cnn_version').text
            server = root_node.find('server')
            self._server_addr = server.find('addr').text
            self._server_port = server.find('port').text
            self._server_api_update = server.find('update_api').text
            self._server_api_check_version = server.find('check_version_api').text
            self._update_cnn_model_api = server.find('update_cnn_model_api').text
        else:
            print(f'не найден {self.file_path}')

    @property
    def model_cnn_name(self):
        return self._model_cnn_name
    @property
    def model_cnn_path(self):
        return self._model_cnn_path
    @property
    def update_cnn_model_api(self):
        return self._update_cnn_model_api

    @property
    def model_cnn_version(self):
        return self._model_cnn_version

    @property
    def update_installer_exe_path(self):
        p = os.path.join(ROOT_DIR, self._update_installer_exe_path)
        return os.path.normcase(p)
    @property
    def app_update_folder(self):
        p = os.path.join(ROOT_DIR, self._app_update_folder)
        return os.path.normcase(p)

    @property
    def get_root_dir(self):
        ROOT_DIR__A = ''  # This is your Project Root
        if getattr(sys, 'frozen', False):
            ROOT_DIR__A = os.path.dirname(sys.executable)
        elif __file__:
            ROOT_DIR__A = os.path.dirname(__file__)
        # print(ROOT_DIR__A)
        # p = os.path.join(ROOT_DIR__A, '/test123')

        return os.path.normcase(os.path.join(ROOT_DIR))

    @property
    def app_version(self):
        return self._app_version

    @property
    def exe_file_main(self):
        return self._exe_file_main

    @property
    def server_addr(self):
        # print(self._server_addr)
        return self._server_addr

    @property
    def server_port(self):
        return self._server_port

    @property
    def server_api_update(self):
        return self._server_api_update

    @property
    def server_api_check_version(self):
        return self._server_api_check_version

    def get_API(self):
        return f'http://{self.server_addr}:{self.server_port}/'

    @property
    def get_coefficient_k(self):
        return float(self._coefficient_k)


if __name__ == '__main__':
    r = ReadXmlProject()
    print(r.get_coefficient_k)
