import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt
from random import randint, choice


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(400, 300)
        canvas.fill(Qt.white)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        self.last_x, self.last_y = None, None
        self.polygon = []

    def mousePressEvent(self, event):
        canvas = self.label.pixmap()
        localPos = event.scenePosition()
        if self.last_x is None:
            self.last_x = localPos.x()
            self.last_y = localPos.y()

        painter = QtGui.QPainter(canvas)
        pen = QtGui.QPen()
        pen.setWidth(10)
        pen.setColor(QtGui.QColor('green'))
        painter.setPen(pen)
        painter.drawPoint(localPos.x(), localPos.y())
        painter.drawLine(self.last_x, self.last_y, localPos.x(), localPos.y())
        self.polygon.append(localPos.x())
        self.polygon.append(localPos.y())
        print(self.polygon)
        painter.end()
        self.label.setPixmap(canvas)
        self.last_x = localPos.x()
        self.last_y = localPos.y()


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()