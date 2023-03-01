import sys
from ast import literal_eval

import cv2
import numpy as np
from PySide6 import QtGui, QtWidgets, QtCore
from PySide6.QtCore import Qt, QPointF, QRectF, QSize, QLineF
from PySide6.QtCore import Slot, Signal
from PySide6.QtGui import QPixmap, QBrush, QColor, QPainterPath
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, \
    QPushButton, QGraphicsScene, QGraphicsItem, QGraphicsView, QGraphicsEllipseItem, QGraphicsLineItem, \
    QGraphicsPolygonItem, QGraphicsPathItem

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
        self.points: list[QPointF] = QPointF()
        self.pen = None
        self.brush = None
        self.path: QGraphicsPolygonItem = QGraphicsPolygonItem()


class Canvas(QtWidgets.QGraphicsView):
    area_signal = Signal(float)

    def __init__(self, image_original: QPixmap = None):
        super().__init__()

        if image_original is None:
            pixmap = QtGui.QPixmap(512, 512)
            pixmap.fill(Qt.gray)
        else:
            pixmap = image_original

        self.scene_canvas = QtWidgets.QGraphicsScene()
        self.scene_canvas.setSceneRect(pixmap.rect())
        self.scene_canvas.addPixmap(pixmap)
        print(self.scene_canvas.event)

        self.original_image_copy = pixmap.copy()
        self.setScene(self.scene_canvas)
        self.id_history_count = 0
        self.history_list: list[historyCanvas] = []
        self.points_local: list[QPointF] = []
        self.pen_local = None
        self.brush = None
        print(self.scene_canvas.sceneRect().getRect())
        # self.setMaximumSize(512, 512)
        self.delta_scale = 1

    def getPolygon(self):
        polygon = []
        if self.history_list:
            for i in self.history_list:
                sssss = []
                if i.path:
                    if i.path.polygon():
                        print(type(i.path.polygon()))
                        for kkk in i.path.polygon():
                            sssss.append(kkk.x())
                            sssss.append(kkk.y())
                if sssss:
                    polygon.append(sssss)
        return polygon

    def getAreaFromPolygon(self):
        p = self.getPolygon()
        summ_area = 0
        for i in p:
            xy = np.array(i)
            print(xy)
            sssssssss = int(len(xy) / 2)
            print(sssssssss)
            xy = xy.reshape((sssssssss, 2))
            xy = xy.astype(int)
            summ_area += cv2.contourArea(xy)
        return summ_area

    def clearScene(self):
        self.scene_canvas.clear()
        self.scene_canvas.addPixmap(self.original_image_copy)

    def clear_canvas(self):
        self.clearScene()
        # self.setPixmap(self.pixmap_clean)
        self.points_local = []
        self.history_list = []
        print('clear_canvas')
        self.area_signal.emit(self.getAreaFromPolygon())

    def cancel_stage(self):
        # Отменить не замкнутый контур

        pen = self.get_pen()
        brush = self.get_brush()
        rad = 1
        scale = pen.width() * 2

        canvas = self.scene_canvas
        self.clearScene()
        if self.points_local:
            del self.points_local[-1]
            for i in range(len(self.points_local) - 1):
                print(self.points_local[i])
                point = QGraphicsEllipseItem(self.points_local[i].x() - rad - scale,
                                             self.points_local[i].y() - rad - scale, rad * scale * 2, rad * scale * 2)
                point.setPen(pen)
                point.setBrush(brush)
                line = QGraphicsLineItem(QLineF(self.points_local[i], self.points_local[i + 1]))
                line.setPen(pen)
                canvas.addItem(point)
                canvas.addItem(line)
            if self.points_local:
                point = QGraphicsEllipseItem(self.points_local[-1].x() - rad - scale,
                                             self.points_local[-1].y() - rad - scale,
                                             rad * scale * 2, rad * scale * 2)
                point.setPen(pen)
                point.setBrush(brush)
                canvas.addItem(point)

        # Нарисовать все контуры
        def draw_all():
            for i in self.history_list:
                pen = i.pen
                print(pen)
                # painter.setPen(pen)
                # painter.drawPoints(i.points)
                #
                if self.history_list:
                    for point_one in i.points:
                        point = QGraphicsEllipseItem(point_one.x() - rad - scale,
                                                     point_one.y() - rad - scale, rad * scale * 2,
                                                     rad * scale * 2)
                        point.setPen(i.pen)
                        point.setBrush(i.brush)
                        canvas.addItem(point)
                    if i.points:
                        for j in range(len(i.points) - 1):
                            line = QGraphicsLineItem(QLineF(i.points[j], i.points[j + 1]))
                            line.setPen(pen)
                            canvas.addItem(line)
                    if i.path is not None:
                        path = QGraphicsPolygonItem(i.path.polygon())
                        path.setBrush(i.brush)
                        canvas.addItem(path)

        # Найти последнюю историю и удалить последний элемент
        if self.history_list:
            print('3-q')
            # last_history = self.history_list[-1]
            # print(last_history.id_history)
            if not self.points_local:
                if self.history_list[-1].points:
                    del self.history_list[-1].points[-1]
                    self.history_list[-1].path = None

                    self.points_local = self.history_list[-1].points

                else:
                    if len(self.history_list) > 0:
                        del self.history_list[-1]
                        # print(len(self.history_list))
            draw_all()
        #
        # painter.end()
        # self.setPixmap(canvas)
        self.area_signal.emit(self.getAreaFromPolygon())

    def close_countor(self):

        h = historyCanvas()
        h.pen = self.get_pen()
        h.brush = self.get_brush()
        canvas = self.scene_canvas
        brush = self.get_brush()

        if self.points_local:
            start = self.points_local[0]
            end = self.points_local[-1]
            if len(self.history_list):
                h.id_history = self.history_list[-1].id_history + 1
            else:
                h.id_history = 0
            h.points = self.points_local
            h.points.append(start)
            self.history_list.append(h)

            line = QGraphicsLineItem(QLineF(start, end))
            line.setPen(self.get_pen())

            print(self.points_local)
            self.history_list[-1].path.setPolygon(self.points_local)
            path = QGraphicsPolygonItem(self.history_list[-1].path.polygon())
            path.setBrush(brush)

            self.points_local = []

            canvas.addItem(line)
            canvas.addItem(path)
            self.area_signal.emit(self.getAreaFromPolygon())



    def set_pen(self, width, color):
        pen = QtGui.QPen()
        pen.setWidth(width)
        pen.setColor(color)

        self.pen_local = pen

    def get_pen(self) -> QtGui.QPen:
        return self.pen_local

    def set_brush(self, color):
        brush = QBrush(color)
        self.brush = brush

    def get_brush(self):
        return self.brush

    def mousePressEvent(self, event):
        brush = self.get_brush()
        super(Canvas, self).mousePressEvent(event)
        canvas = self.scene_canvas
        localPos = self.mapToScene(event.position().toPoint())
        pen = self.get_pen()
        rad = 1
        scale = pen.width() * 2
        if self.scene_canvas.sceneRect().height() > localPos.x() > 0 and self.scene_canvas.sceneRect().width() > localPos.y() > 0:
            point = QGraphicsEllipseItem(localPos.x() - rad - scale, localPos.y() - rad - scale, rad * scale * 2,
                                         rad * scale * 2)
            point.setBrush(brush)
            point.setPen(pen)
            # print(self.get_pen().color().getRgb())
            if len(self.points_local):
                line = QGraphicsLineItem(QLineF(self.points_local[-1], localPos))
                line.setPen(pen)
                canvas.addItem(line)
            canvas.addItem(point)
            self.points_local.append(localPos.toPoint())
            # print(localPos.toPoint())

    def zoom_plus(self):
        # print(self.)
        self.delta_scale += 0.2
        self.scale(1.25, 1.25)
        print('plus')

    def zoom_minus(self):
        if self.delta_scale > 0.5:
            self.scale(0.8, 0.8)
            self.delta_scale -= 0.2
        print('minus')
        print(self.delta_scale)


class DrawingCounter(QDialog):
    image_result_edit_doctor = Signal(QPixmap)
    history_n_n = Signal(HistoryNeuralNetwork)

    def __init__(self, image_original=None, parent=None):
        super(DrawingCounter, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        if image_original is not None:
            self.c = Canvas(image_original=image_original)
        else:
            self.c = Canvas()


        self.c.area_signal.connect(self.on_edit_area)

        self.ui.verticalLayout.addWidget(self.c)
        self.c.set_pen(3, QtGui.QColor(255, 0, 0))
        self.c.set_brush(QColor(0, 0, 127, 100))

        self.ui.cancel_button.clicked.connect(self.c.cancel_stage)
        self.ui.clear_countor_button.clicked.connect(self.c.clear_canvas)
        self.ui.countor_close_button.clicked.connect(self.c.close_countor)
        self.ui.zoom_plus.clicked.connect(self.c.zoom_plus)
        self.ui.zoom_minus.clicked.connect(self.c.zoom_minus)
        self.ui.cancel_button.setEnabled(True)
        self.ui.clear_countor_button.setEnabled(True)
        self.ui.save_button.clicked.connect(self.c.getPolygon)
        self.ui.save_button.clicked.connect(self.c.getAreaFromPolygon)

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
        self.path = QPainterPath()
        self.polygon_QPoint = []
        # self.ui.save_button.clicked.connect(self.on_click_save_image_button)
        # self.history = HistoryNeuralNetwork()
        # self.categorical = self.get_predict_categorical()
        # self.ui.select_categorical_disease_button.clicked.connect(self.select_disease)
        # self.color_brush_r = 0
        # self.color_brush_g = 0
        # self.color_brush_b = 0

    @Slot(int)
    def on_edit_area(self, area):
        self.ui.area_countor_label.setText(f'Площадь: {str(area)}')

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
