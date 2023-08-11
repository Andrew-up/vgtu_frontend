from ast import literal_eval
from matplotlib import pyplot
from PySide6.QtCore import QByteArray, QBuffer
from PySide6.QtGui import QImage, QPixmap


def image_to_base64(Qimage):
    image = QImage(Qimage)
    data = QByteArray()
    buf = QBuffer(data)
    image.save(buf, 'PNG')
    res = data.toBase64()
    # base64_to_image(res)

    return str(res)


import base64
import io
from PIL import Image


# def is_valid_base_64(base64):


def is_valid_base64_image(image_string):
    try:
        im_bytes = base64.b64decode(image_string)  # im_bytes is a binary image
        im_file = io.BytesIO(im_bytes)  # convert image to file-like object
        img = Image.open(im_file)  # img is now PIL Image object

        print('file is valid base64 image')
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
    image_bytes = base64.b64decode(byteArray)
    img = QImage.fromData(image_bytes)
    image = QPixmap.fromImage(img)
    return image


if __name__ == '__main__':
    pass
    # f = string.encode('utf-8')
    # print(f)
    # print(eval(string))
    # res = is_valid_base64_image(eval(string))
    # print(res)
