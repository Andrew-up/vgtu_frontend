import sys

import cv2
import numpy as np
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QApplication, QRadioButton, \
    QPushButton, QVBoxLayout, QDialog, QLabel

from model.result_predict import ResultPredict
from service.PatientService import get_categorical_predict


class CustomRadioButtonClass(QRadioButton):
    clickButtonItem = Signal(int)

    def __init__(self, camera_index: int):
        super().__init__()
        self.index_cam = camera_index
        self.setText(f'Камера : {camera_index}')
        self.clicked.connect(lambda: self.clickButtonItem.emit(self.index_cam))


class SelectedCamera(QDialog):
    clickButtonItem = Signal(int)

    def __init__(self):
        super(SelectedCamera, self).__init__()
        self.label = QLabel()
        arr = self.returnCameraIndexes()
        layout = QVBoxLayout()
        if arr:
            for i in arr:
                radio = CustomRadioButtonClass(camera_index=i)
                radio.clickButtonItem.connect(self.on_selected_category)
                layout.addWidget(radio)
            save_button = QPushButton()
            save_button.setText("Сохранить")
            save_button.clicked.connect(self.on_save_button_click)
            layout.addWidget(save_button)
        else:
            save_button = QPushButton()
            save_button.setText("Закрыть")
            save_button.clicked.connect(self.close)
            layout.addWidget(self.label)
            layout.addWidget(save_button)

        self.selected_camera_index = -1
        self.setLayout(layout)


    def on_selected_category(self, item: int):
        self.selected_camera_index = item


    def on_save_button_click(self):
        self.clickButtonItem.emit(self.selected_camera_index)
        # print(self.selected_camera_index)
        self.close()


    def returnCameraIndexes(self):
        # checks the first 3 indexes.
        index = 0
        arr = []
        i = 3
        while i > 0:
            cap = cv2.VideoCapture(index, cv2.CAP_DSHOW)
            for jjjj in range(10):
                cap.read()
            success, img = cap.read()
            if success:
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                all_pixels = gray.shape[0] * gray.shape[1]
                bright_count = np.sum(np.array(gray) > 127)
                a = (bright_count/all_pixels * 100)
                p = f'Камер не обнаружно, или слишком темно. \n Процент пикселей значение которых выше 127: {round(a, 2)} % '
                self.label.setText(p)
                if a > 10:
                    arr.append(index)
            cap.release()
            cv2.destroyAllWindows()
            index += 1
            i -= 1
        return arr



if __name__ == '__main__':
    app = QApplication()
    window = SelectedCamera()
    window.show()
    sys.exit(app.exec())
