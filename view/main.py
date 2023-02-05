import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget

from service.slotsService import SlotsMainMenu
from view.py.mainwindow import Ui_MainWindow
from view.user.list_patient_widget import ListPatient

class MainWindow(QMainWindow):
    this_class_slot = SlotsMainMenu()

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.this_class_slot.open_start_view.connect(self.open_start_view)
        self.this_class_slot.set_widget_main_menu.connect(self.set_widget_root_stacket_widget)
        self.view_patient()

    def view_patient(self):
        list_patient = ListPatient(self)
        list_patient.set_main_menu_slots(self.this_class_slot)
        list_patient.get_all_patient()
        self.this_class_slot.set_widget_main_menu.emit(list_patient)

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
