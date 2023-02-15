from PySide6 import QtGui
from PySide6.QtCore import Slot, QSize, Signal
from PySide6.QtGui import QPixmap, QImage, QBrush, QColor, QPainterPath
from PySide6.QtWidgets import QWidget, QApplication, QMessageBox, QFrame, QLabel, QDialog
import sys
from view.py.draw_counter_widget import Ui_Form
from PySide6.QtCore import Qt


class DrawingCounter(QDialog):

    image_result_edit_doctor = Signal(QPixmap)

    def __init__(self, image_original = None, parent=None):
        super(DrawingCounter, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        canvas = QtGui.QPixmap(512, 512)
        canvas.fill(Qt.white)
        self.polygon = []
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

    def on_click_save_image_button(self):
        print('save')
        self.image_result_edit_doctor.emit(self.ui.image_drawing_canvas.pixmap())


    def on_close_contour(self):
        canvas = self.canvas.pixmap()
        pen = QtGui.QPen()
        pen.setWidth(5)
        pen.setColor(QtGui.QColor('green'))
        painter = QtGui.QPainter(canvas)
        painter.setPen(pen)
        painter.drawLine(self.last_x, self.last_y, self.first_x, self.first_y)
        self.path.addPolygon(self.polygon_QPoint)
        print(self.path)
        painter.fillPath(self.path, QBrush(QColor(0, 255, 0, 100)))
        painter.end()
        self.canvas.setPixmap(canvas)
        self.last_x = None
        self.last_y = None
        self.polygon_QPoint.clear()
        self.path.clear()

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
        pen.setColor(QtGui.QColor('green'))
        painter.setPen(pen)
        painter.drawPoint(localPos.x(), localPos.y())
        painter.drawLine(self.last_x, self.last_y, localPos.x(), localPos.y())
        self.polygon.append(localPos.x())
        self.polygon.append(localPos.y())
        print(self.polygon)
        print(localPos)
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
