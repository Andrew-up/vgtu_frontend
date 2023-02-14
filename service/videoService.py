import time

from PySide6.QtCore import QThread, Signal, Qt
from PySide6.QtGui import QImage
import cv2
import numpy as np

class VideoWorker(QThread):

    changePixmap = Signal(QImage)
    play_video = True
    cam_num = 0

    def opencvFormatToQImage(self, image: QImage):
        # print(image)
        convertToQtFormats = QImage(image.data, image.shape[1], image.shape[0],
                                    QImage.Format.Format_BGR888)
        qimage = convertToQtFormats.scaled(512, 512, Qt.KeepAspectRatio)
        return qimage

    def run(self):
            print(self.play_video)
            cap = cv2.VideoCapture(self.cam_num, cv2.CAP_DSHOW)
            while True:
                if self.play_video:
                    ret, frame = cap.read()
                    self.changePixmap.emit(self.opencvFormatToQImage(frame))
                else:
                    cap.release()
                    cv2.destroyAllWindows()
                    print('поток закончен')
                    break



