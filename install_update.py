import os.path
import shutil
import subprocess
import sys
import time
import tkinter as tk
import xml.etree.ElementTree as ET
import zipfile
from threading import Thread
from tkinter import BOTH, ttk, END, RIGHT, Y, WORD
from ast import literal_eval

class Worker(Thread):
    OK = 0
    ERROR = -1

    def __init__(self,
                 path_temp=None,
                 path_target=None,
                 txt=tk.Text,
                 root: tk.Tk = None,
                 name_archive=None,
                 start_main_exe=False,
                 parent=None):
        super(Worker, self).__init__(parent)
        self._file_name_archive = name_archive
        self.txt = txt
        self.root = root
        self._start_main_exe = start_main_exe
        self._path_temp = os.path.join(path_temp)
        self._path_target = os.path.join(path_target)
        self.create_path_target()
        self.zip_file_temp_full_path = f'{self._path_temp}/{self._file_name_archive}'


    def create_path_target(self):
        if os.path.exists(self._path_target):
            self.add_text(f"папка {self._path_target} есть")
        else:
            os.mkdir(self._path_target)
            self.add_text(f"создал папку{self._path_target}")

    def add_text(self, str):
        txt.pack(expand=1, fill=BOTH)
        txt.insert(END, str + '\n')

    def unpack_zip_file(self):
        self.add_text('Идет распаковка файлов')
        try:
            with zipfile.ZipFile(self.zip_file_temp_full_path, 'r') as zip_file:
                try:
                    self.add_text('пытаюсь распаковать')
                    zip_file.extractall(f'{self._path_temp}')
                    self.add_text('распаковка успешна')
                    return self.OK
                except zipfile.BadZipfile as e:
                    self.add_text('распаковка ошибка')
                    self.add_text(str(e))
                    return self.ERROR

        except BaseException as e:
            self.add_text('Ошибка: \n' + str(e))
            return self.ERROR

    def run(self):
        print('--------------')
        status = self.unpack_zip_file()
        # append_text_list("Поток загружен")
        time.sleep(1)
        if status is self.OK:
            try:
                self.add_text(f"Копирую файлы из {self._path_temp} в {self._path_target}")
                self.add_text('--------------------------')
                time.sleep(1)
                self.add_text(self._path_temp)
                files = os.listdir(self._path_temp)
                self.add_text('--------------------------')
                time.sleep(1)
                files.remove(self._file_name_archive)
                # print(files)
                # time.sleep(4)
                for i in files:
                    self.add_text(i)
                    shutil.copy(self._path_temp + '/' + str(i), self._path_target)
                self.add_text('Копирование закончилось')
                time.sleep(1)
                print('копирование закончилось')

            except OSError as e:
                print(e)
            if self._start_main_exe:
                main_path = os.path.join(self._path_target, 'main.exe')
                if os.path.exists(main_path):
                    try:
                        self.add_text('Запускаю новую версию')
                        subprocess.run(main_path)
                        # os.remove(self.zip_file_temp_full_path)
                    except subprocess.CalledProcessError as e:
                        self.add_text(str(e.output))
                else:
                    self.add_text(f'Файл: {main_path} не найден')
            else:
                self.add_text(f'Запуск main.exe == : {self._start_main_exe}')
        else:
            self.add_text(f'Не удалось распаковать архив, проверьте каталог\n'
                          f'{self.zip_file_temp_full_path}')


def get_update_dir_from_xml():
    ROOT_DIR = ''  # This is your Project Root
    if getattr(sys, 'frozen', False):
        ROOT_DIR = os.path.dirname(sys.executable)
    elif __file__:
        ROOT_DIR = os.path.dirname(__file__)

    xml = ROOT_DIR + '/project.xml'
    if os.path.exists(xml):
        root_node = ET.parse(xml).getroot()
        app = root_node.find('app')
        update_dir = app.find('temp_update').text
        name_archive = app.find('file_name_archive').text
        return os.path.join(ROOT_DIR, update_dir), ROOT_DIR, name_archive


def add_text(str):
    txt.pack(expand=1, fill=BOTH)
    txt.insert(END, str + '\n')


if __name__ == '__main__':
    print('11111111')
    update_dir, ROOT_DIR, file_name_archive = get_update_dir_from_xml()
    print('2222222222')

    root = tk.Tk()
    root.geometry("500x400")
    root.title("Обновление")
    root.deiconify()
    root.focus()
    txt = tk.Text(root, wrap=WORD)

    # вертикальная прокрутка
    scrollbar = ttk.Scrollbar(orient="vertical", command=txt.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    txt.config(yscrollcommand=scrollbar.set)

    path_temp, path_target, start_main_exe = None, None, None
    if len(sys.argv) > 2:
        path_temp = sys.argv[1]
        path_target = sys.argv[2]
        start_main_exe = literal_eval(sys.argv[3])

    if path_temp is not None and path_target is not None:
        add_text('Получил аргументы при запуске программы: ')
        add_text(path_temp)
        add_text(path_target)
        w = Worker(path_temp=path_temp, path_target=path_target, name_archive=file_name_archive, root=root, start_main_exe=start_main_exe)
        w.daemon = True
        w.start()
    else:
        add_text('Получил аргументы по умолчанию:')
        add_text(update_dir)
        add_text(ROOT_DIR)
        w = Worker(path_temp=update_dir, path_target=ROOT_DIR, name_archive=file_name_archive, root=root)
        w.daemon = True
        w.start()

    root.mainloop()
