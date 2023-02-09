import os
import sys
import time
import zipfile

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QMessageBox

from service.slotsService import SlotsMainMenu
from view.py.mainwindow import Ui_MainWindow
from view.user.list_patient_widget import ListPatient
from controller.UpdateAppController import UpdateApp
import subprocess
from definitions import EXE, ZIP_FILE_NEW, ROOT_DIR, DEBUG_MODE, EXE_NEW
from updater import upd


class MainWindow(QMainWindow):
    this_class_slot = SlotsMainMenu()

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.this_class_slot.open_start_view.connect(self.open_start_view)
        self.this_class_slot.set_widget_main_menu.connect(self.set_widget_root_stacket_widget)
        self.view_patient()
        self.ui.pushButton.clicked.connect(self.update_app)


        # Обновление приложения в отдельном потоке
        self.updated = UpdateApp()
        self.updated.signal_download_ok.connect(self.restart_app)


    def view_patient(self):
        list_patient = ListPatient(self)
        list_patient.set_main_menu_slots(self.this_class_slot)
        list_patient.get_all_patient()
        self.this_class_slot.set_widget_main_menu.emit(list_patient)

    @Slot()
    def update_app(self):
        self.close()
        upd()
        # self.updated.start()

    @Slot()
    def restart_app(self):
        print('Перезагрузаю приложение')
        msg = QMessageBox()
        msg.setInformativeText("Обновление скачано, перезапустить приложение?")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setWindowTitle("Установка обновлений")
        msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)
        res = msg.exec()
        if res == QMessageBox.StandardButton.Yes:
            self.close()
            time.sleep(0.2)
            main_file = ROOT_DIR + f'/main.exe'
            with zipfile.ZipFile(ZIP_FILE_NEW, 'r') as zip_file:
                if DEBUG_MODE:
                    print('DEBUG MODE ON')
                    os.remove(ROOT_DIR + '/dist/main/main.exe')
                    zip_file.extractall(f'{ROOT_DIR}/dist/main/')
                    print(ROOT_DIR + f'/dist/main/main.exe')
                else:
                    try:
                        print('DEBUG MODE OFF')
                        time.sleep(2)
                        # os.remove(main_file)
                        time.sleep(2)
                        print(ZIP_FILE_NEW)
                        zip_file.extractall(f'{ROOT_DIR}')
                        time.sleep(2)
                    except Exception as e:
                        print(ZIP_FILE_NEW)
                        print(e)
                        time.sleep(10)
            time.sleep(2)
            try:
                print(main_file)
                time.sleep(2)
                subprocess.Popen([main_file])
            except Exception as e:
                print(e)
                time.sleep(10)
            time.sleep(2)

        if res == QMessageBox.StandardButton.Cancel:
            print('Отмена удаления')

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
        if self.getCountStacketWidget() > 100:
            pages = self.ui.stacked_widget_main.count()
            for i in range(pages):
                widget = self.ui.stacked_widget_main.widget(0)
                self.ui.stacked_widget_main.removeWidget(widget)
            print('сработала очистка stacked widget')
        else:
            print('Еще рано очищать stacked widget')


if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
