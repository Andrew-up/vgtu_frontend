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
from model.Annotations import Annotations
from service.PatientService import PatientServiceFront
from service.imageService import image_to_base64
from view.py.draw_counter_widget import Ui_Form
from view.user.catrgorical_item_widget import CategoricalItem
from itertools import cycle
from utils.message_box import message_error_show
from utils.read_xml_file import ReadXmlProject

from itertools import groupby


class TypeHistory(enum.Enum):
    null = 0
    line = 1
    point = 2
    polygon = 3
    rect = 4


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
    area_signal = Signal(str)
    cancel_button_signal = Signal(bool)
    save_button_signal = Signal(bool)
    contour_close_button_signal = Signal(bool)
    clear_contour_button_signal = Signal(bool)
    open_select_diagnosis = Signal()

    def __init__(self, image_original: QPixmap = None):
        super().__init__()

        if image_original is None:
            pixmap = QtGui.QPixmap(128, 512)
            pixmap.fill(Qt.gray)

        else:
            pixmap = image_original
            # print(image_original.rect())



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
        self.annotation_list: list[Annotations] = []
        self._result_predict: ResultPredict = ResultPredict()

    @property
    def result_predict(self) -> ResultPredict:
        return self._result_predict

    @result_predict.setter
    def result_predict(self, value):
        self._result_predict = value

    def get_image_from_scene(self):
        image = QImage(int(self.scene_canvas.width()), int(self.scene_canvas.height()),
                       QImage.Format_ARGB32_Premultiplied)
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

    def polygonToNumpyArray(self, polygon):
        if polygon:
            xy = np.array(polygon)
            sssssssss = int(len(xy) / 2)
            xy = xy.reshape((sssssssss, 2))
            xy = xy.astype(int)
            return xy
    def getAreaFromPolygon(self, polygon):
        summ_area = 0.0
        if polygon:
            xy = self.polygonToNumpyArray(polygon)
            summ_area = float(cv2.contourArea(xy))
        return float(summ_area)

    def clearScene(self):
        self.scene_canvas.clear()
        self.scene_canvas.addPixmap(self.original_image_copy)

    def clear_canvas(self):
        self.clearScene()
        self.item_history = []
        self.list_item_history = []
        self.save_button_signal.emit(False)
        self.cancel_button_signal.emit(False)
        self.clear_contour_button_signal.emit(False)
        self.contour_close_button_signal.emit(False)
        self.annotation_list = []
        # print(self.getAreaFromPolygon([]))
        self.area_signal.emit(str(self.getAreaFromPolygon([])))

    def cancel_stage(self):
        if not self.item_history and self.list_item_history:
            if self.list_item_history[-1].list_history:
                self.item_history = self.list_item_history[-1].list_history
                del self.list_item_history[-1]
                if self.annotation_list:
                    print(len(self.annotation_list))
                    del self.annotation_list[-1]
                    self.sum_annotation_list()



        if self.item_history:
            if self.item_history[-1].type == TypeHistory.polygon:
                self.scene_canvas.removeItem(self.item_history[-1].item_history)
                del self.item_history[-1]

        if self.item_history:
            if self.item_history[-1].type == TypeHistory.rect:
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
        # self.area_signal.emit(self.getAreaFromPolygon())

        if not self.item_history and not self.list_item_history:
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

    def sum_annotation_list(self):
        string_res = str()
        coefficient_k = ReadXmlProject().get_coefficient_k
        if self.annotation_list:
            sort_list = sorted(self.annotation_list, key=lambda x: x.category_id)
            for key, groups_item in groupby(sort_list, key=lambda x: x.category_id):
                sum = 0.0
                category_ru: str = str()
                for item in groups_item:
                    sum += item.area
                    category_ru = item.result_predict.name_category_ru
                string_res += category_ru + ' ' + str(float(round(sum*coefficient_k, 2))) + 'кв мм, '
            self.area_signal.emit(string_res)

    def close_countor(self):
        sum_points = 0
        pen = self.get_pen()
        rad = 1
        scale = pen.width() * 2
        canvas = self.scene_canvas
        a = Annotations()
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

                polygon_xy = []
                for i in polygon.polygon():
                    polygon_xy.append(i.x())
                    polygon_xy.append(i.y())
                a.segmentation = polygon_xy
                a.area = self.getAreaFromPolygon(polygon_xy)
                array_np = self.polygonToNumpyArray(polygon_xy)
                bbox = cv2.boundingRect(array_np)
                x, y, w, h = bbox
                rect = QGraphicsRectItem(x, y, w, h)
                self.scene_canvas.addItem(rect)
                self.add_history(rect, TypeHistory.rect)
                self.add_history(polygon, TypeHistory.polygon)
                a.bbox = [x, y, w, h]
                if self.list_item_history:
                    listzzzzzzzzz = ListHistoryCanvasTwo(self.list_item_history[-1].id_list_history + 1,
                                                         self.item_history, polygon)
                else:
                    listzzzzzzzzz = ListHistoryCanvasTwo(0, self.item_history, polygon)
                self.list_item_history.append(listzzzzzzzzz)
                self.item_history = []

        self.contour_close_button_signal.emit(False)
        self.save_button_signal.emit(True)

        if self.annotation_list:
            a.id_annotations = self.annotation_list[-1].id_annotations + 1
            print(a.id_annotations)
        a.category_id = self.result_predict.id_category
        a.history_nn_id = None
        a.result_predict = self.result_predict
        self.annotation_list.append(a)
        self.sum_annotation_list()

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
                self.open_select_diagnosis.emit()
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
            # print(f'height: {self.scene_canvas.sceneRect().height()}')
            # print(f'width: {self.scene_canvas.sceneRect().width()}')
            # print(f'x: {localPos.x()}')
            # print(f'y: {localPos.y()}')
            if self.scene_canvas.sceneRect().width() > localPos.x() > 0 and \
                    self.scene_canvas.sceneRect().height() > localPos.y() > 0:
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
    annotation_signal = Signal(Annotations)

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
        self.canvas.open_select_diagnosis.connect(self.select_disease)

        self.ui.verticalLayout.addWidget(self.canvas)
        self.ui.cancel_button.clicked.connect(self.canvas.cancel_stage)
        self.ui.clear_countor_button.clicked.connect(self.canvas.clear_canvas)
        self.ui.countor_close_button.clicked.connect(self.canvas.close_countor)
        self.ui.zoom_plus.clicked.connect(self.canvas.zoom_plus)
        self.ui.zoom_minus.clicked.connect(self.canvas.zoom_minus)
        self.ui.cancel_button.setEnabled(True)
        self.ui.clear_countor_button.setEnabled(True)

        self.ui.save_button.clicked.connect(self.canvas.getAreaFromPolygon)
        self.ui.save_button.clicked.connect(self.on_click_save_image_button)
        self.history_n_n = HistoryNeuralNetwork()
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

    @Slot(str)
    def on_edit_area(self, string):
        self.ui.area_countor_label.setText(f'Площадь: {string}')
        self.ui.area_countor_label.setWordWrap(True)

    def select_disease(self):

        if self.canvas.get_len_item_history() != 0:
            message_error_show(self, message='Вначале замкните контур текущей болезни', title='Ошибка')
            return 0
        dlg = CategoricalItem()
        dlg.clickButtonItem.connect(self.ooooooooooooooooo)
        dlg.exec()

    @Slot(ResultPredict)
    def ooooooooooooooooo(self, result_predict: ResultPredict):
        self.ui.type_disease_label.setText('Сейчас выбрано: ' + result_predict.name_category_ru)
        r, g, b = literal_eval(result_predict.color)
        self.color.setRgb(r, g, b)
        self.canvas.set_pen(3, self.color)
        self.canvas.set_brush(QColor(r, g, b, 127))
        self.canvas.result_predict = result_predict

    def on_click_save_image_button(self):
        self.history_n_n.annotations.clear()

        for i in self.canvas.annotation_list:
            a = Annotations(**i.__dict__)
            a.result_predict = ResultPredict(**i.result_predict.__dict__)
            # print('==========anns==========')
            # print(a)
            self.history_n_n.annotations.append(a)
        qiamge = self.canvas.get_image_from_scene()

        self.history_n_n.photo_predict_edit_doctor = image_to_base64(qiamge)
        self.image_result_edit_doctor.emit(QPixmap.fromImage(qiamge))
        self.annotation_signal.emit(self.history_n_n.annotations)


        # self.history_n_n.annotations.clear()
        # for i in self.canvas.annotation_list:
        #     print(type(i.category))
        #     a = Annotations(**i.__dict__)
        #     a.category = ResultPredict(**i.category.__dict__).__dict__
        #     self.history_n_n.annotations.append(a.__dict__)
        # print(self.history_n_n.__dict__)

        # Не удалять
        # image = self.canvas.get_image_from_scene()
        # print(type(image))
        # if self.history is not None:
        #     self.history.polygon_mask = self.canvas.getPolygon()
        #     qiamge = self.canvas.original_image_copy
        #     self.history.photo_predict_edit_doctor = image_to_base64(qiamge.toImage())
        #     self.history.area_wound = self.canvas.getAreaFromPolygon()
        #     self.history_n_n.emit(self.history)
        # self.image_result_edit_doctor.emit(QPixmap.fromImage(image))
        self.close()


if __name__ == '__main__':
    app = QApplication()
    window = DrawingCounter()
    window.show()
    sys.exit(app.exec())
