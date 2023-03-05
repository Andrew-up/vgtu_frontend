import enum
import sys
from ast import literal_eval

import cv2
import numpy as np
from PySide6 import QtGui, QtWidgets, QtCore
from PySide6.QtCore import Qt, QPointF, QRectF, QSize, QLineF
from PySide6.QtCore import Slot, Signal
from PySide6.QtGui import QPixmap, QBrush, QColor, QPainterPath, QPen, QPainter, QImage
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, \
    QPushButton, QGraphicsScene, QGraphicsItem, QGraphicsView, QGraphicsEllipseItem, QGraphicsLineItem, \
    QGraphicsPolygonItem, QGraphicsPathItem, QGraphicsRectItem

from model.history_neural_network import HistoryNeuralNetwork
from model.result_predict import ResultPredict
from service.PatientService import PatientServiceFront
from service.imageService import image_to_base64
from view.py.draw_counter_widget import Ui_Form
from view.user.catrgorical_item_widget import CategoricalItem
from itertools import cycle
from utils.message_box import message_error_show
from utils.read_xml_file import ReadXmlProject

class TypeHistory(enum.Enum):
    null = 0
    line = 1
    point = 2
    polygon = 3


class HistoryCanvasTwo(object):
    def __init__(self):
        self.id_history: int = 0
        self.item_history: QGraphicsItem() = None
        self.type: TypeHistory = TypeHistory.null


class ListHistoryCanvasTwo(object):

    def __init__(self, list_history_id, list_history_item, polygon):
        self.id_list_history: int = list_history_id
        self.list_history: list[HistoryCanvasTwo()] = list_history_item
        self.polygon: QGraphicsPolygonItem() = polygon


class Canvas(QtWidgets.QGraphicsView):
    area_signal = Signal(int)

    cancel_button_signal = Signal(bool)
    save_button_signal = Signal(bool)
    contour_close_button_signal = Signal(bool)
    clear_contour_button_signal = Signal(bool)

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
        self.original_image_copy = pixmap.copy()
        self.setScene(self.scene_canvas)
        self.pen_local: QPen = QPen(QColor(0, 0, 0))
        self.brush: QBrush = QBrush(QColor(0, 0, 0, 127))
        self.delta_scale = 1
        self.item_history: list[HistoryCanvasTwo] = []
        self.list_item_history: list[ListHistoryCanvasTwo] = []
        self.default_pen = True


    def get_image_from_scene(self):
        image = QImage(int(self.scene_canvas.width()), int(self.scene_canvas.height()), QImage.Format_ARGB32_Premultiplied)
        painter = QPainter(image)
        self.scene_canvas.render(painter)
        painter.end()
        return image
        # self.scene_canvas.render()

    def get_len_item_history(self):
        return len(self.item_history)

    def get_len_list_item_history(self):
        return len(self.list_item_history)

    def get_count_points(self):
        sum_point = 0
        for i in self.item_history:
            if i.type == TypeHistory.point:
                sum_point += 1
        return sum_point

    def getPolygon(self):
        polygon = []
        if self.list_item_history:
            for i in self.list_item_history:
                sssss = []
                if i.polygon:
                    if i.polygon.polygon():
                        for kkk in i.polygon.polygon():
                            sssss.append(kkk.x())
                            sssss.append(kkk.y())
                if sssss:
                    polygon.append(sssss)
        return polygon

    def getAreaFromPolygon(self):
        coefficient_k = ReadXmlProject().get_coefficient_k
        p = self.getPolygon()
        summ_area: float = 0
        for i in p:
            xy = np.array(i)
            sssssssss = int(len(xy) / 2)
            xy = xy.reshape((sssssssss, 2))
            xy = xy.astype(int)
            x, y, w, h = cv2.boundingRect(xy)
            rect = QGraphicsRectItem(x, y, w, h)
            self.scene_canvas.addItem(rect)

            summ_area += int(cv2.contourArea(xy))
        summ_area = summ_area * coefficient_k
        return int(summ_area)

    def clearScene(self):
        self.scene_canvas.clear()
        self.scene_canvas.addPixmap(self.original_image_copy)

    def clear_canvas(self):
        self.clearScene()
        self.item_history = []
        self.list_item_history = []
        self.area_signal.emit(self.getAreaFromPolygon())
        self.save_button_signal.emit(False)
        self.cancel_button_signal.emit(False)
        self.clear_contour_button_signal.emit(False)
        self.contour_close_button_signal.emit(False)

    def cancel_stage(self):
        if not self.item_history and self.list_item_history:
            if self.list_item_history[-1].list_history:
                self.item_history = self.list_item_history[-1].list_history
                del self.list_item_history[-1]

        if self.item_history:
            if self.item_history[-1].type == TypeHistory.polygon:
                self.scene_canvas.removeItem(self.item_history[-1].item_history)
                del self.item_history[-1]
        if self.item_history:
            if self.item_history[-1].type == TypeHistory.point:
                self.scene_canvas.removeItem(self.item_history[-1].item_history)
                del self.item_history[-1]
        if self.item_history:
            if self.item_history[-1].type == TypeHistory.line:
                self.scene_canvas.removeItem(self.item_history[-1].item_history)
                del self.item_history[-1]
        self.area_signal.emit(self.getAreaFromPolygon())

        if not self.item_history and not self.list_item_history:
            # print('zzzzzzzzzzzzzzzz')
            self.save_button_signal.emit(False)
            self.cancel_button_signal.emit(False)
            self.clear_contour_button_signal.emit(False)
            self.contour_close_button_signal.emit(False)
        if self.get_count_points() <= 2:
            self.contour_close_button_signal.emit(False)
        if self.get_count_points() > 2:
            self.contour_close_button_signal.emit(True)
        self.save_button_signal.emit(False)
        if self.list_item_history and not self.item_history:
            self.save_button_signal.emit(True)


    def close_countor(self):

        sum_points = 0
        pen = self.get_pen()
        rad = 1
        scale = pen.width() * 2
        canvas = self.scene_canvas

        for i in self.item_history:
            if i.type == TypeHistory.point:
                sum_points += 1

        if sum_points >= 3:
            if self.item_history[-1].type == TypeHistory.point:
                xy_start_point = QPointF(self.item_history[0].item_history.rect().x() + rad + scale,
                                         self.item_history[0].item_history.rect().y() + rad + scale)
                xy_end_point = QPointF(self.item_history[-1].item_history.rect().x() + rad + scale,
                                       self.item_history[-1].item_history.rect().y() + rad + scale)
                # print('points >= 3')
                point = QGraphicsEllipseItem()
                point.setBrush(self.get_brush())
                point.setPen(pen)
                point.setRect(self.item_history[0].item_history.rect().x(),
                              self.item_history[0].item_history.rect().y(),
                              rad * scale * 2, rad * scale * 2)
                line = QGraphicsLineItem(QLineF(xy_start_point, xy_end_point))
                line.setPen(pen)
                canvas.addItem(line)
                self.add_history(line, TypeHistory.line)
                self.add_history(point, TypeHistory.point)

        if sum_points >= 3:
            if self.item_history[-1].type == TypeHistory.point:
                polygon_points: list[QPointF] = []
                polygon: QGraphicsPolygonItem = QGraphicsPolygonItem()
                for i in self.item_history:
                    if i.type == TypeHistory.point:
                        xy = QPointF(i.item_history.rect().x() + rad + scale, i.item_history.rect().y() + rad + scale)
                        polygon_points.append(xy)
                polygon.setPolygon(polygon_points)
                polygon.setBrush(self.get_brush())
                canvas.addItem(polygon)
                self.add_history(polygon, TypeHistory.polygon)
                if self.list_item_history:
                    listzzzzzzzzz = ListHistoryCanvasTwo(self.list_item_history[-1].id_list_history + 1,
                                                         self.item_history, polygon)
                else:
                    listzzzzzzzzz = ListHistoryCanvasTwo(0, self.item_history, polygon)
                self.list_item_history.append(listzzzzzzzzz)
                self.item_history = []

        self.area_signal.emit(self.getAreaFromPolygon())
        self.contour_close_button_signal.emit(False)
        self.save_button_signal.emit(True)
        # print(self.getPolygon())


    def set_pen(self, width, color):
        pen = QtGui.QPen()
        pen.setWidth(width)
        pen.setColor(color)
        self.pen_local = pen
        self.default_pen = False

    def get_pen(self) -> QtGui.QPen:
        return self.pen_local

    def set_brush(self, color):
        brush = QBrush(color)
        self.brush = brush

    def get_brush(self):
        return self.brush

    def add_history(self, item, type):
        history: HistoryCanvasTwo = HistoryCanvasTwo()
        if self.item_history:
            history.id_history = self.item_history[-1].id_history + 1
        else:
            history.id_history = 0
        history.item_history = item
        history.type = type
        self.item_history.append(history)

    def mousePressEvent(self, event):
        self.save_button_signal.emit(False)
        if event.button() == Qt.MouseButton.LeftButton:
            if self.default_pen:
                message_error_show(self, message='Укажите категорию болезни', title='Ошибка')
                return 0
            brush = self.get_brush()
            super(Canvas, self).mousePressEvent(event)
            if self.get_count_points() >= 2:
                self.contour_close_button_signal.emit(True)
            canvas = self.scene_canvas
            localPos = self.mapToScene(event.position().toPoint()).toPoint()
            # print(localPos)
            pen = self.get_pen()
            rad = 1
            scale = pen.width() * 2
            # print(localPos)
            if self.scene_canvas.sceneRect().height() > localPos.x() > 0 and \
                    self.scene_canvas.sceneRect().width() > localPos.y() > 0:
                point_pos_x, point_pos_y = localPos.x() - scale - rad, localPos.y() - scale - rad
                point = QGraphicsEllipseItem()
                point.setBrush(brush)
                point.setPen(pen)
                point.setRect(point_pos_x, point_pos_y, rad * scale * 2, rad * scale * 2)
                # print(len(self.item_history))
                if self.item_history:
                    # print(self.item_history[-1].type)
                    if self.item_history[-1].type == TypeHistory.point:
                        xy_start_point = QPointF(self.item_history[-1].item_history.rect().x() + rad + scale,
                                                 self.item_history[-1].item_history.rect().y() + rad + scale)
                        # print(self.item_history[-1].item_history.rect().getRect())
                        # print(xy_start_point)
                        line = QGraphicsLineItem(QLineF(xy_start_point, localPos))
                        line.setPen(pen)
                        canvas.addItem(point)
                        canvas.addItem(line)
                        self.add_history(line, TypeHistory.line)
                        self.add_history(point, TypeHistory.point)
                else:
                    canvas.addItem(point)
                    self.add_history(point, TypeHistory.point)
                    # self.save_button_signal.emit(True)
                    self.cancel_button_signal.emit(True)
                    self.clear_contour_button_signal.emit(True)
                    # print(point.rect().getRect())


        if event.button() == Qt.MouseButton.RightButton:
            self.cancel_stage()

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
        # print(self.delta_scale)


class DrawingCounter(QDialog):
    image_result_edit_doctor = Signal(QPixmap)
    history_n_n = Signal(HistoryNeuralNetwork)

    def __init__(self, image_original=None, parent=None):
        super(DrawingCounter, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        if image_original is not None:
            self.canvas = Canvas(image_original=image_original)
        else:
            self.canvas = Canvas()

        self.canvas.area_signal.connect(self.on_edit_area)
        self.canvas.clear_contour_button_signal.connect(self.clear_contour_button_isEnabled)
        self.canvas.cancel_button_signal.connect(self.cancel_button_button_isEnabled)
        self.canvas.save_button_signal.connect(self.save_button_isEnabled)
        self.canvas.contour_close_button_signal.connect(self.contour_close_button_isEnabled)

        self.ui.verticalLayout.addWidget(self.canvas)

        self.ui.cancel_button.clicked.connect(self.canvas.cancel_stage)
        self.ui.clear_countor_button.clicked.connect(self.canvas.clear_canvas)
        self.ui.countor_close_button.clicked.connect(self.canvas.close_countor)
        self.ui.zoom_plus.clicked.connect(self.canvas.zoom_plus)
        self.ui.zoom_minus.clicked.connect(self.canvas.zoom_minus)
        self.ui.cancel_button.setEnabled(True)
        self.ui.clear_countor_button.setEnabled(True)
        self.ui.save_button.clicked.connect(self.canvas.getPolygon)
        self.ui.save_button.clicked.connect(self.canvas.getAreaFromPolygon)
        self.ui.save_button.clicked.connect(self.on_click_save_image_button)

        self.history = HistoryNeuralNetwork()
        self.categorical = self.get_predict_categorical()
        self.ui.select_categorical_disease_button.clicked.connect(self.select_disease)
        self.color = QColor()

        self.ui.cancel_button.setEnabled(False)
        self.ui.save_button.setEnabled(False)
        self.ui.countor_close_button.setEnabled(False)
        self.ui.clear_countor_button.setEnabled(False)



    @Slot(bool)
    def save_button_isEnabled(self, b):
        if b:
            self.ui.save_button.setEnabled(True)
        else:
            self.ui.save_button.setEnabled(False)

    @Slot(bool)
    def contour_close_button_isEnabled(self, b):
        if b:
            self.ui.countor_close_button.setEnabled(True)
        else:
            self.ui.countor_close_button.setEnabled(False)

    @Slot(bool)
    def clear_contour_button_isEnabled(self, b):
        if b:
            self.ui.clear_countor_button.setEnabled(True)
        else:
            self.ui.clear_countor_button.setEnabled(False)

    @Slot(bool)
    def cancel_button_button_isEnabled(self, b):
        if b:
            self.ui.cancel_button.setEnabled(True)
        else:
            self.ui.cancel_button.setEnabled(False)

    @Slot(int)
    def on_edit_area(self, area):
        print(area)
        self.ui.area_countor_label.setText(f'Площадь: {str(area)}')

    def select_disease(self):
        # print(self.c.get_len_item_history())
        # print(self.c.get_len_list_item_history())
        if self.canvas.get_len_item_history() + self.canvas.get_len_list_item_history() != 0:
            message_error_show(self, message='Можно указать только 1 болезнь\n Очистите рисинок от других', title='Ошибка')
            return 0
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
        r, g, b = literal_eval(category.color)
        self.color.setRgb(r, g, b)
        self.canvas.set_pen(3, self.color)
        self.canvas.set_brush(QColor(r, g, b, 127))

    def get_predict_categorical(self) -> list[ResultPredict]:
        return PatientServiceFront(1).get_all_categorical()

    def on_click_save_image_button(self):
        image = self.canvas.get_image_from_scene()
        print(type(image))
        # print('save')
        # print(self.history.result_predict)
        if self.history is not None:
            self.history.polygon_mask = self.canvas.getPolygon()
            qiamge = self.canvas.original_image_copy
            self.history.photo_predict_edit_doctor = image_to_base64(qiamge.toImage())
            self.history.area_wound = self.canvas.getAreaFromPolygon()
            self.history_n_n.emit(self.history)
        self.image_result_edit_doctor.emit(QPixmap.fromImage(image))
        self.close()


if __name__ == '__main__':
    app = QApplication()
    window = DrawingCounter()
    window.show()
    sys.exit(app.exec())
