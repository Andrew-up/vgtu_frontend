import base64

from PySide6 import QtGui, QtCore
from PySide6.QtCore import QByteArray, QBuffer
from PySide6.QtGui import QImage

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


def is_valid_base64_image(image_string):
    # checking valid base64 image string
    try:
        image = base64.b64decode(eval(image_string))
        img = Image.open(io.BytesIO(image))
    except Exception:
        print('file is not valid base64 image')
        return False

    # checking image format I want to support
    if img.format.lower() in ["jpg", "jpeg", "png"]:

        # if you need to check image dimension
        width, height = img.size
        if width < 800 and height < 800:
            return True
        else:
            print('image size exceeded, width and height must be less than 800 pixels')
            return False
        # end of checking dimentions

    else:
        print('Image is not valid, only \'base64\' image (jpg, jpeg, png) is valid')



def base64_to_image(base64_image):
    # print(base64_image)
    basad = QByteArray.fromBase64(eval(base64_image))
    img = QImage.fromData(basad, 'PNG')

    # pil_img_image = ImageQt.fromqimage(img)
    # pil_img_image.show()

    # print(type(img))
    return img


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
        base64.b64decode(eval(s)).decode('utf-8')
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

