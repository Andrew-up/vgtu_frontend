import base64
import json
from ast import literal_eval

from PySide6 import QtGui, QtCore
from PySide6.QtCore import QByteArray, QBuffer
from PySide6.QtGui import QImage, QPixmap

from PIL import ImageQt


def image_to_base64(Qimage):
    image = QImage(Qimage)
    data = QByteArray()
    buf = QBuffer(data)
    image.save(buf, 'PNG')
    res = data.toBase64()
    base64_to_image(res)

    return str(res)


import base64
import io
from PIL import Image

# def is_valid_base_64(base64):


def is_valid_base64_image(image_string):

    try:
        string = image_string[1:-1]
        image = base64.b64decode(string)
        img = Image.open(io.BytesIO(image))
        return True
    except Exception:
        print('file is not valid base64 image')
        return False



def base64_to_image(base64_image):
    # print(base64_image)
    basad = QByteArray.fromBase64(base64_image)
    img = QImage.fromData(basad, 'PNG')

    # pil_img_image = ImageQt.fromqimage(img)
    # pil_img_image.show()

    # print(type(img))
    return img


def byteArrayToPixmap(byteArray):
    basad = QByteArray.fromBase64(literal_eval(byteArray))
    img = QImage.fromData(basad, 'PNG')
    image = QPixmap.fromImage(img)
    return image


class ImageConverter(object):
    def __init__(self, parent=None):
        super(ImageConverter, self).__init__(parent)

    def qpixmap_to_qimage(self):
        return 'qimage'

    def qimage_qpixmap(self):
        return 'qpixmap'


def stringIsBase64(s):
    # print(type(s))
    try:
        base64.b64decode(literal_eval(s)).decode('utf-8')
        return True
    except Exception:
        return False


if __name__ == '__main__':
    pass
    # f = string.encode('utf-8')
    # print(f)
    # print(eval(string))
    # res = is_valid_base64_image(eval(string))
    # print(res)

