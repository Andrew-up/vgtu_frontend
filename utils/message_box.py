from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMessageBox


@Slot(str)
def message_error_show(parent, message):
    msg = QMessageBox(parent=parent)
    msg.setText(f'{message}')
    msg.setIcon(QMessageBox.Icon.Critical)
    msg.exec()


@Slot(str)
def message_info_show(parent, message):
    msg = QMessageBox(parent=parent)
    msg.setText(f'{message}')
    msg.setIcon(QMessageBox.Icon.Information)
    msg.exec()
