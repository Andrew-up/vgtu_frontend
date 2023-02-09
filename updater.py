import os
import subprocess
import time
import zipfile

from definitions import EXE, ZIP_FILE_NEW, ROOT_DIR, DEBUG_MODE, EXE_NEW


def upd():
    with zipfile.ZipFile(ZIP_FILE_NEW, 'r') as zip_file:
        try:
            print('пытаюсь распаковать')
            zip_file.extractall(f'{ROOT_DIR}')
            print('распаковка успешна')
        except BaseException as e:
            print('распаковка ошибка')
            print(e)
    print('Пытаюсь запустить Exe файл')
    subprocess.Popen(["python main.py"])
