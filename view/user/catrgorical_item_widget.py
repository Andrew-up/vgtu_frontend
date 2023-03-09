import sys

from PySide6.QtCore import Qt, Signal, Slot
from PySide6.QtWidgets import QWidget, QApplication, QLabel, QListWidget, QListWidgetItem, QHBoxLayout, QRadioButton, \
    QButtonGroup, QPushButton, QVBoxLayout

from model.result_predict import ResultPredict


class JJJJJ(QRadioButton):

    clickButtonItem = Signal(str)

    def __init__(self, name=None):
        super().__init__()
        self.setText(str(name))
        self.id = name
        self.button_description = 'this_button id : ' + str(self.id)
        self.clicked.connect(lambda: self.clickButtonItem.emit(self.button_description))


class CategoricalItem(QWidget):
    clickButtonItem = Signal(ResultPredict)

    def __init__(self, layout: QVBoxLayout = None, category: ResultPredict = None):
        super(CategoricalItem, self).__init__()
        q_radio = QRadioButton()
        self.cat_pred = None
        self.color = None
        self.index = []
        if category is not None:
            self.color = category.color
            self.cat_pred = category
            q_radio.setText(category.name_category_ru)
        q_radio.clicked.connect(self.clickghdhgfs)

        if layout is None:
            layout = QVBoxLayout()
            for i in range(5):
                pass
                q_radiosss = JJJJJ(i)
                q_radiosss.clickButtonItem.connect(self.prohfdhgf)
                layout.addWidget(q_radiosss)
            self.setLayout(layout)
        else:
            layout.addWidget(q_radio)

    def prohfdhgf(self, item):
        print(item)

    def clickghdhgfs(self):
        if self.cat_pred is not None:
            self.clickButtonItem.emit(self.cat_pred)


if __name__ == '__main__':
    app = QApplication()
    window = CategoricalItem()
    window.show()
    sys.exit(app.exec())
