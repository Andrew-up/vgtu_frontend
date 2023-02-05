from PySide6.QtCore import Signal, QThread, QObject
from PySide6.QtWidgets import QWidget

class SlotsMainMenu(QObject):
    open_start_view = Signal()
    set_widget_main_menu = Signal(QWidget)
    test_signal3 = Signal()
    test_signal4 = Signal()

