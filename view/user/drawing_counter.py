import sys
from ast import literal_eval

import cv2
import numpy as np
from PySide6 import QtGui, QtWidgets, QtCore
from PySide6.QtCore import Qt, QPointF
from PySide6.QtCore import Slot, Signal
from PySide6.QtGui import QPixmap, QBrush, QColor, QPainterPath
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, \
    QPushButton, QGraphicsScene, QGraphicsItem, QGraphicsView

from model.history_neural_network import HistoryNeuralNetwork
from model.result_predict import ResultPredict
from service.PatientService import PatientServiceFront
from service.imageService import image_to_base64
from view.py.draw_counter_widget import Ui_Form
from view.user.catrgorical_item_widget import CategoricalItem
from itertools import cycle

class historyCanvas(object):
    def __init__(self):
        self.id_history: int = 0
        self.points = None
        self.pen = None
        self.lines = None



class Canvas(QtWidgets.QLabel):

    def __init__(self):
        super().__init__()
        pixmapsss = QtGui.QPixmap(600, 300)
        pixmapsss.fill(Qt.white)
        self.pixmap_clean = pixmapsss.copy()
        self.setPixmap(pixmapsss)
        self.id_history_count = 0
        self.history_list: list[historyCanvas] = []
        self.points_local = []
        self.pen_local = None


    def clear_canvas(self):
        self.setPixmap(self.pixmap_clean)
        print('clear_canvas')


    # def cancel_stage(self):
    #     if len(self.history_list) > 0:
    #         self.setPixmap(self.pixmap_clean)
    #         canvas = self.pixmap()
    #         painter = QtGui.QPainter(canvas)
    #         del self.history_list[-1]
    #         max_point = len(self.history_list)
    #         id_point = 0
    #         for i in range(len(self.history_list)):
    #             pen = self.history_list[i].pen
    #             painter.setPen(pen)
    #             painter.drawPoint(self.history_list[i].point)
    #             id_point += 1
    #             if max_point > id_point:
    #                 painter.drawLine(self.history_list[i].point, self.history_list[i + 1].point)
    #         painter.end()
    #         self.setPixmap(canvas)
    def cancel_stage(self):
        self.setPixmap(self.pixmap_clean)
        canvas = self.pixmap()
        painter = QtGui.QPainter(canvas)
        local = False
        if self.points_local:
            del self.points_local[-1]
            pen = self.pen_local
            painter.setPen(pen)
            painter.drawPoints(self.points_local)
            local = True
            max_point = len(self.points_local)
            for i in range(len(self.points_local)):
                if i < max_point:
                    print(f'i: {i}')
                    print(f'max_point: {max_point}')
                    # print(self.points_local[i+1])
                    painter.drawLine(self.points_local[i], self.points_local[i-1])


        for i in self.history_list:
            pen = i.pen
            painter.setPen(pen)
            painter.drawPoints(i.points)

        if not local:
            if self.history_list:
                last = self.history_list[-1]
                print(last.points)
                if last.points:
                    del last.points[-1]
                    print(last)
                    pen = last.pen
                    painter.setPen(pen)
                    for i in range(len(last.points)):
                        painter.drawPoint(last.points[i])

                if not last.points:
                    print('11111111')
                    del self.history_list[-1]






        painter.end()
        self.setPixmap(canvas)



        # pass



    def close_countor(self):

        h = historyCanvas()
        start = self.points_local[0]
        end = self.points_local[-1]
        if len(self.history_list):
            h.id_history = self.history_list[-1].id_history + 1
        else:
            h.id_history = 0

        h.points = self.points_local
        h.pen = self.pen_local
        self.history_list.append(h)

        canvas = self.pixmap()
        painter = QtGui.QPainter(canvas)
        painter.setPen(h.pen)
        painter.drawLine(start, end)
        painter.end()
        self.setPixmap(canvas)
        self.points_local = []
        print(self.history_list[-1].id_history)





    # def close_countor(self):
    #     self.history_list.points.append(self.points_local)
    #     self.history_list.pen = self.pen_local
    #     print(self.history_list.points)
    #     start = self.points_local[0]
    #     end = self.points_local[-1]
    #     print(start)
    #     print(end)
    #     canvas = self.pixmap()
    #     painter = QtGui.QPainter(canvas)
    #     painter.setPen(self.history_list.pen)
    #     painter.drawLine(start, end)
    #     painter.end()
    #     self.setPixmap(canvas)
    #
    #     self.points_local = []
    #     # h = historyCanvas()
    #     # h.point = end
    #     # h.id_history = self.id_history_count = self.id_history_count + 1
    #     # h.pen = self.history_list[0].pen
    #     # self.history_list.append(h)


    def mousePressEvent(self, event):
        super(Canvas, self).mousePressEvent(event)
        canvas = self.pixmap()
        # painter = QtGui.QPainter(canvas)
        localPos = self.mapFrom(self, event.position())
        painter = QtGui.QPainter(canvas)
        pen = QtGui.QPen()
        pen.setWidth(15)
        pen.setColor(QtGui.QColor(255, 0, 0))
        painter.setPen(pen)
        painter.drawPoint(localPos.x(), localPos.y())
        # print(len(self.history_list))
        self.pen_local = pen
        if len(self.points_local):
            painter.drawLine(self.points_local[-1], localPos)

        painter.end()
        self.setPixmap(canvas)
        self.points_local.append(localPos)

        # h = historyCanvas()
        # h.points.append(localPos)
        # h.id_history = self.id_history_count = self.id_history_count + 1
        # h.pen = pen
        # self.history_list.points.append(localPos)
        # print(self.history_list[-1].points)


class DrawingCounter(QDialog):
    image_result_edit_doctor = Signal(QPixmap)
    history_n_n = Signal(HistoryNeuralNetwork)

    def __init__(self, image_original=None, parent=None):
        super(DrawingCounter, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.c = Canvas()
        self.ui.verticalLayout.addWidget(self.c)
        self.ui.cancel_button.clicked.connect(self.c.cancel_stage)
        self.ui.clear_countor_button.clicked.connect(self.c.clear_canvas)
        self.ui.countor_close_button.clicked.connect(self.c.close_countor)
        self.ui.cancel_button.setEnabled(True)
        self.ui.clear_countor_button.setEnabled(True)

        # self.polygon = []
        # self.polygon_all = []
        # self.last_x, self.last_y = None, None
        # self.first_x, self.first_y = None, None
        # self.canvas = self.ui.image_drawing_canvas
        # self.image_edit = image_original
        # if image_original is not None:
        #     self.ui.image_drawing_canvas.setPixmap(image_original)
        #     # self.ui.image_drawing_canvas.setScaledContents(True)
        # else:
        #     self.ui.image_drawing_canvas.setPixmap(canvas)
        # self.ui.countor_close_button.clicked.connect(self.on_close_contour)
        # self.path = QPainterPath()
        # self.polygon_QPoint = []
        # self.ui.save_button.clicked.connect(self.on_click_save_image_button)
        # self.history = HistoryNeuralNetwork()
        # self.categorical = self.get_predict_categorical()
        # self.ui.select_categorical_disease_button.clicked.connect(self.select_disease)
        # self.color_brush_r = 0
        # self.color_brush_g = 0
        # self.color_brush_b = 0

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
        sssssssss = int(len(xy) / 2)
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

    # def mousePressEvent(self, event):

    # canvas = self.canvas.pixmap()
    # print(canvas.size())
    # localPos = event.scenePosition()
    # if self.last_x is None:
    #     self.last_x = localPos.x()
    #     self.last_y = localPos.y()
    #     self.first_x, self.first_y = localPos.x(), localPos.y()

    #     painter = QtGui.QPainter(canvas)
    #     pen = QtGui.QPen()
    #     pen.setWidth(5)
    #     pen.setColor(QtGui.QColor(self.color_brush_r, self.color_brush_g, self.color_brush_b))
    #
    #     painter.setPen(pen)
    #     painter.drawPoint(localPos.x(), localPos.y())
    #     painter.drawLine(self.last_x, self.last_y, localPos.x(), localPos.y())
    #     self.polygon.append(localPos.x())
    #     self.polygon.append(localPos.y())
    #     # print(self.polygon)
    #     print(localPos)
    #     self.polygon_QPoint.append(localPos)
    #     painter.end()
    #     self.canvas.setPixmap(canvas)
    #     self.last_x = localPos.x()
    #     self.last_y = localPos.y()


if __name__ == '__main__':
    app = QApplication()
    window = DrawingCounter()
    window.show()
    sys.exit(app.exec())
