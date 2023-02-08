import time

import requests
import os

from PySide6.QtCore import Slot, Signal, QThread

IpV4 = '188.235.18.191'
port = 8095
API = f'http://{IpV4}:{port}/'
import shutil

from definitions import ZIP_FILE_NEW

class UpdateApp(QThread):
    signal_download_ok = Signal()

    def __init__(self, parent=None):
        super(UpdateApp, self).__init__(parent)

    def run(self):
        print("======== ЗАГРУЖАЮ ОБНОВЛЕНИЕ =======")
        time.sleep(0.5)
        str_url = f'{API}app/update/'
        response = requests.get(str_url, stream=True)
        print(ZIP_FILE_NEW)
        with open(ZIP_FILE_NEW, 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
            time.sleep(0.2)
            print('ok')
            self.signal_download_ok.emit()


if __name__ == '__main__':
    # update_this_app()
    pass