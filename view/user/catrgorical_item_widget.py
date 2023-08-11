import sys

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QApplication, QRadioButton, \
    QPushButton, QVBoxLayout, QDialog

from model.result_predict import ResultPredict
from service.PatientService import get_categorical_predict


class CustomRadioButtonClass(QRadioButton):
    clickButtonItem = Signal(ResultPredict)

    def __init__(self, category: ResultPredict):
        super().__init__()
        self.cat = category
        self.setText(category.name_category_ru)
        self.clicked.connect(lambda: self.clickButtonItem.emit(self.cat))


class CategoricalItem(QDialog):
    clickButtonItem = Signal(ResultPredict)

    def __init__(self):
        super(CategoricalItem, self).__init__()
        self.result_predict = get_categorical_predict()
        layout = QVBoxLayout()
        for i in self.result_predict:
            radio = CustomRadioButtonClass(category=i)
            radio.clickButtonItem.connect(self.on_selected_category)
            layout.addWidget(radio)
        self.save_button = QPushButton()
        self.save_button.setText("Сохранить")
        self.save_button.clicked.connect(self.on_save_button_click)
        layout.addWidget(self.save_button)
        self.setWindowTitle('Выберите категорию')
        self.setLayout(layout)
        self.selected_category = ResultPredict()

    def on_selected_category(self, item: ResultPredict):
        self.selected_category = item

    def on_save_button_click(self):
        self.clickButtonItem.emit(self.selected_category)
        print(self.selected_category.name_category_ru)
        self.close()

    def get_all_category(self) -> list[ResultPredict]:
        return get_categorical_predict()


if __name__ == '__main__':
    app = QApplication()
    window = CategoricalItem()
    window.show()
    sys.exit(app.exec())
