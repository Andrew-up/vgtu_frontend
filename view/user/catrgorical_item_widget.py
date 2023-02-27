import sys

from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QWidget, QApplication, QLabel, QListWidget, QListWidgetItem, QHBoxLayout, QRadioButton, \
    QButtonGroup, QPushButton, QVBoxLayout

from model.result_predict import ResultPredict


class CategoricalItem(QWidget):

    clickButtonItem = Signal(ResultPredict)

    def __init__(self, layout: QVBoxLayout = None, category: ResultPredict = None):
        super(CategoricalItem, self).__init__()
        q_radio = QRadioButton()
        self.cat_pred = None
        self.color = None
        if category is not None:
            self.color = category.color
            self.cat_pred = category
            q_radio.setText(category.name_category_ru)
        q_radio.clicked.connect(self.clickghdhgfs)
        layout.addWidget(q_radio)


    def clickghdhgfs(self):
        if self.cat_pred is not None:
            self.clickButtonItem.emit(self.cat_pred)






if __name__ == '__main__':
    app = QApplication()
    window = CategoricalItem()
    window.show()
    sys.exit(app.exec())
