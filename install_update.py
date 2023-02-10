import shutil
import subprocess
import sys
import time
from threading import Thread
import os.path
import tkinter as tk
from tkinter import BOTH, YES, ttk, END, RIGHT, Y



# def append_text_list(str):



class Worker(Thread):
    def __init__(self, path_temp=None, path_target=None, listbox: tk.Listbox = None, root: tk.Tk = None, parent=None):
        super(Worker, self).__init__(parent)
        self.root = root
        self.listbox = listbox
        self._path_temp = os.path.join(path_temp)
        self._path_target = os.path.join(path_target)


    def add_list_box(self, str):
        self.listbox.insert(END, str)
        self.listbox.pack(anchor='s', fill=BOTH, expand=True)

    def run(self):
        print('--------------')
        # append_text_list("Поток загружен")
        print('22222222')
        try:
            self.add_list_box(f"Копирую файлы из {self._path_temp} в {self._path_target}")
            self.add_list_box('--------------------------')
            files = os.listdir(self._path_temp)
            time.sleep(4)
            for i in files:
                self.add_list_box(i)
                shutil.copy(self._path_temp + '/' + str(i), self._path_target)

            self.add_list_box('Копирование закончилось')
            print('копирование закончилось')
            self.add_list_box('Запускаю новую версию')

        except OSError as e:
            print(e)
        # time.sleep(4)
        subprocess.Popen(os.path.join(self._path_target, 'main.exe'))
        # self.root.quit()



def startappppps():

    root = tk.Tk()
    root.geometry("500x400")
    root.title("Обновление")
    listbox = tk.Listbox()

    # вертикальная прокрутка
    scrollbar = ttk.Scrollbar(orient="vertical", command=listbox.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    listbox["yscrollcommand"] = scrollbar.set

    path_temp, path_target = 'E:\\vgtu\\vgtu_frontend\\temp_update', 'E:\\vgtu\\vgtu_frontend'
    w = Worker(path_temp=path_temp, path_target=path_target, listbox=listbox, root=root)
    w.daemon = False
    w.start()
    # print(scrollbar)
    root.mainloop()

if __name__ == '__main__':

    startappppps()
    # tessddddt()
    # path_temp, path_target = 'E:\\vgtu\\vgtu_frontend\\temp_update', 'E:\\vgtu\\vgtu_frontend'
    # if len(sys.argv) > 2:
    #     path_temp = sys.argv[1]
    #     path_target = sys.argv[2]
    #
    # print(path_temp)
    # print(path_target)
    #
    # if path_temp is not None and path_target is not None:
    #
    #     print('GO Поток')
    #     w = Worker(path_temp=path_temp, path_target=path_target)
    #     w.daemon = True
    #     w.start()
    #     print('GO Поток 2')
    #     root.mainloop()
    # else:
    #     print('Передайте пути для копирования в аргументы')
