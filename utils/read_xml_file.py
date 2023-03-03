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
        self._init_variable()


    def _init_variable(self):
        if os.path.exists(self.file_path):
            root_node = ET.parse(self.file_path).getroot()
            app = root_node.find('app')
            self._app_update_folder = app.find('temp_update').text
            self._app_version = app.find('version').text
            self._coefficient_k = app.find('coefficient_k').text
            server = root_node.find('server')

            self._server_addr = server.find('addr').text
            self._server_port = server.find('port').text
            self._server_api_update = server.find('update_api').text
            self._server_api_check_version = server.find('check_version_api').text
        else:
            print(f'не найден {self.file_path}')

    @property
    def app_version(self):
        return self._app_version

    @property
    def app_exe_fil_main(self):
        return self._app_exe_file_main

    @property
    def app_update_folder(self):
        return self._app_update_folder

    @property
    def server_addr(self):
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
