from ast import literal_eval

import cv2
import numpy as np
from PySide6 import QtGui
from PySide6.QtCore import Slot, QSize, Signal
from PySide6.QtGui import QPixmap, QImage, QBrush, QColor, QPainterPath
from PySide6.QtWidgets import QWidget, QApplication, QMessageBox, QFrame, QLabel, QDialog, QListWidget, QVBoxLayout, QPushButton
import sys

from service.PatientService import PatientServiceFront
from view.py.draw_counter_widget import Ui_Form
from PySide6.QtCore import Qt
from model.history_neural_network import HistoryNeuralNetwork
from service.imageService import ImageConverter, image_to_base64
from model.result_predict import ResultPredict
from view.user.catrgorical_item_widget import CategoricalItem
import collections

class DrawingCounter(QDialog):

    image_result_edit_doctor = Signal(QPixmap)
    history_n_n = Signal(HistoryNeuralNetwork)

    def __init__(self, image_original = None, parent=None):
        super(DrawingCounter, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        canvas = QtGui.QPixmap(512, 512)
        canvas.fill(Qt.white)
        self.polygon = []
        self.polygon_all = []
        self.last_x, self.last_y = None, None
        self.first_x, self.first_y = None, None
        self.canvas = self.ui.image_drawing_canvas
        self.image_edit = image_original
        if image_original is not None:
            self.ui.image_drawing_canvas.setPixmap(image_original)
            self.ui.image_drawing_canvas.setScaledContents(True)
        else:
            self.ui.image_drawing_canvas.setPixmap(canvas)
        self.ui.countor_close_button.clicked.connect(self.on_close_contour)
        self.path = QPainterPath()
        self.polygon_QPoint = []
        self.ui.save_button.clicked.connect(self.on_click_save_image_button)
        self.history = HistoryNeuralNetwork()
        self.categorical = self.get_predict_categorical()
        self.ui.select_categorical_disease_button.clicked.connect(self.select_disease)
        self.color_brush_r = 0
        self.color_brush_g = 0
        self.color_brush_b = 0


    def select_disease(self):
        dlg = QDialog()
        layout = QVBoxLayout()
        for i in self.categorical:
            item = CategoricalItem(layout, category=i)
            item.clickButtonItem.connect(self.ooooooooooooooooo)
            layout.addWidget(item)
        save_button = QPushButton()
        save_button.setText("Сохранить")
        save_button.clicked.connect(dlg.close)
        layout.addWidget(save_button)
        dlg.setLayout(layout)
        dlg.exec()

    @Slot(ResultPredict)
    def ooooooooooooooooo(self, category: ResultPredict):
        self.history.result_predict_id = category.id_category
        self.history.result_predict = category
        self.ui.type_disease_label.setText(category.name_category_ru)
        self.color_brush_r, self.color_brush_g, self.color_brush_b, = literal_eval(category.color)

    def get_predict_categorical(self) -> list[ResultPredict]:
        return PatientServiceFront(1).get_all_categorical()

    def on_click_save_image_button(self):
        print('save')
        print(self.history)
        if self.history is not None:
            self.history.polygon_mask = self.polygon_all
            qiamge = self.ui.image_drawing_canvas.pixmap().toImage()
            self.history.photo_predict_edit_doctor = image_to_base64(qiamge)
            self.history_n_n.emit(self.history)
        self.image_result_edit_doctor.emit(self.ui.image_drawing_canvas.pixmap())
        self.close()


    def on_close_contour(self):
        canvas = self.canvas.pixmap()
        pen = QtGui.QPen()
        pen.setWidth(5)
        pen.setColor(QtGui.QColor(self.color_brush_r, self.color_brush_g, self.color_brush_b))
        painter = QtGui.QPainter(canvas)
        painter.setPen(pen)
        painter.drawLine(self.last_x, self.last_y, self.first_x, self.first_y)
        self.path.addPolygon(self.polygon_QPoint)
        # print(self.path)
        painter.fillPath(self.path, QBrush(QColor(self.color_brush_r, self.color_brush_g, self.color_brush_b, 100)))
        painter.end()
        self.canvas.setPixmap(canvas)
        self.last_x = None
        self.last_y = None
        self.polygon_QPoint.clear()
        self.path.clear()
        self.polygon_all.append(self.polygon.copy())
        xy = np.array(self.polygon)
        sssssssss = int(len(xy)/2)
        xy = xy.reshape((sssssssss, 2))
        xy = xy.astype(int)
        # self.area_full += cv2.contourArea(xy)
        # print(self.area_full)
        self.polygon.clear()
        self.history.area_wound += cv2.contourArea(xy)

        # print(self.polygon_all)
        self.ui.area_countor_label.setText('Площадь контура: ' + str(self.history.area_wound))



    def PolyArea(self, x, y):
        return 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))

    def mousePressEvent(self, event):
        canvas = self.canvas.pixmap()
        localPos = event.scenePosition()
        if self.last_x is None:
            self.last_x = localPos.x()
            self.last_y = localPos.y()
            self.first_x, self.first_y = localPos.x(), localPos.y()

        painter = QtGui.QPainter(canvas)
        pen = QtGui.QPen()
        pen.setWidth(5)
        pen.setColor(QtGui.QColor(self.color_brush_r, self.color_brush_g, self.color_brush_b))
        painter.setPen(pen)
        painter.drawPoint(localPos.x(), localPos.y())
        painter.drawLine(self.last_x, self.last_y, localPos.x(), localPos.y())
        self.polygon.append(localPos.x())
        self.polygon.append(localPos.y())
        # print(self.polygon)
        # print(localPos)
        self.polygon_QPoint.append(localPos)
        painter.end()
        self.canvas.setPixmap(canvas)
        self.last_x = localPos.x()
        self.last_y = localPos.y()



if __name__ == '__main__':
    app = QApplication()
    window = DrawingCounter()
    window.show()
    sys.exit(app.exec())
