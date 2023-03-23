import base64
import os
import random
import time
from ast import literal_eval

import cv2
import numpy as np
from PIL import Image
from PySide6.QtCore import QThread, Signal
from PySide6.QtCore import Qt
from PySide6.QtGui import QImage, QPixmap
from matplotlib import pyplot as plt

from definitions import DATASET_PATH, MODEL_H5_PATH
from model.result_predict import ResultPredict
from model.result_scan import ResultScan
from model.Annotations import Annotations


class LoadingModelAndPredict(QThread):
    loading_model_end = Signal(str)
    predict_image_result = Signal(QPixmap)
    image_original = Signal(QPixmap)
    result_scan = Signal(Annotations)
    video_stream_image = Signal(QImage)
    # Запомнить номер камеры
    number_cam = -1
    play_video = True

    def __init__(self, path_model, parent=None):
        super(LoadingModelAndPredict, self).__init__(parent)
        start = time.time()
        self.model = None
        self.path_model = path_model
        self.segmentation_polygon = None
        self.area = None
        self.image_batch = None
        self.scan_from_cam = False
        self.image_path = None
        self.categorical_predict: list[ResultPredict] = []
        self.list_annotations: list[Annotations] = []

    def set_categorical_predict(self, categorical):
        self.categorical_predict = categorical

    def set_image_path(self, path_image):
        self.image_path = path_image

    def opencvFormatToQImage(self, image: QImage):
        print(image.shape)
        convertToQtFormats = QImage(image.data, image.shape[1], image.shape[0], QImage.Format.Format_BGR888)
        qimage = convertToQtFormats.scaled(512, 512, Qt.KeepAspectRatio)
        return qimage

    def video_stream(self):
        print('streamVideo')
        print(self.play_video)
        cap = cv2.VideoCapture(self.number_cam, cv2.CAP_DSHOW)
        while True:
            if self.play_video:
                ret, frame = cap.read()
                self.video_stream_image.emit(self.opencvFormatToQImage(frame))
            else:
                cap.release()
                cv2.destroyAllWindows()
                print('поток закончен')
                break

    def run(self):
        self.video_stream()
        print('==========___==========')
        image = self.get_image()
        if image is not None:
            # print(image)
            height, width, channel = image.shape
            bytesPerLine = 3 * width
            image_2 = QImage(image, width, height, bytesPerLine, QImage.Format_BGR888)

            pixmap = QPixmap(image_2)
            print(type)
            self.image_original.emit(pixmap)

            print('Началась загрузка модели в отдельном потоке')
            secundomer = time.time()
            self.load_model_func()
            res = round(time.time() - secundomer, 2)
            self.loading_model_end.emit(str(res))  # посылаем сигнал с временем загрузки модели
            image_preprocessing = self.image_preprocessing(image)
            batch_image = self.create_batch(image_preprocessing)
            predict = self.predict(batch_image, image)
            image_qt = self.opencvFormatToQImage(predict)
            self.predict_image_result.emit(QPixmap.fromImage(image_qt))
        else:
            self.video_stream_image.emit(QImage())
        print('Поток закончил свою работу')

    def load_model_func(self):
        from keras.models import load_model
        from utils.unet_model.model_losses import dice_coef, bce_dice_loss, binary_weighted_cross_entropy, MyMeanIOU, \
            dice_loss
        iou1111 = MyMeanIOU(num_classes=12)
        if self.model is None:
            print('------ Загружаю модель ------')
            self.model = load_model(self.path_model,
                                    custom_objects={'dice_loss': dice_loss,
                                                    'MyMeanIOU': iou1111})
            return self.model
        else:
            return self.model

    def get_image(self):
        # Получение картинки с камеры
        print(self.image_path)
        print(self.scan_from_cam)
        if self.image_path is None and self.scan_from_cam:
            print('2222222222')
            timer = time.time()
            cap = cv2.VideoCapture(self.number_cam, cv2.CAP_DSHOW)  # 0 - номер камеры
            # "Прогреваем" камеру, чтобы снимок не был тёмным
            for i in range(30):
                cap.read()
            ret, frame = cap.read()
            if not ret:
                print("failed to grab frame")
            self.image_original.emit(frame)
            cap.release()
            cv2.destroyAllWindows()
            # Возращаем кадр из видеопотока
            return frame
        else:
            print('222222222222')
            print(self.scan_from_cam)
            print(self.image_path)
            if self.scan_from_cam == False and self.image_path is not None:
                # Получаем картинку если картинка из каталога
                # image = cv2.imread(self.image_path, cv2.COLOR_RGB2BGR)
                image = cv2.imread(self.image_path, cv2.COLOR_BGR2RGB)
                return image

    def drawingMaskForImagePredict(self, image: Image, predict: Image, color, result_category: ResultPredict):
        p = cv2.resize(predict, (512, 512), interpolation=cv2.INTER_AREA)
        p = p.astype('uint8')

        polygon, hierarchy = cv2.findContours(p, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        image_original_copy = image.copy()
        polygon_result = []
        if polygon is not None:
            # print(polygon)
            # print(dir(polygon))
            polygon = sorted(polygon, key=cv2.contourArea, reverse=True)
            image_temp = np.zeros_like(image, np.uint8)
            image_original_copy = image.copy()
            print(f'count polygon: {len(polygon)}')

            for contour in polygon:
                # print(contour)
                peri = cv2.arcLength(contour, True)
                if peri > 1:
                    polygon_result.append(cv2.approxPolyDP(contour, 0.01 * peri, True))
                    polygon_annotation = cv2.approxPolyDP(contour, 0.01 * peri, True)
                    box = cv2.boundingRect(contour)
                    cv2.fillPoly(image_temp, pts=[contour], color=color)
                    a = Annotations()
                    a.id_annotations = None
                    a.history_nn_id = None
                    a.segmentation = self.unpackArray(polygon_annotation)
                    x, y, w, h = box
                    a.bbox = [x, y, w, h]
                    a.category_id = result_category.id_category
                    a.category = result_category
                    a.area = cv2.contourArea(polygon_annotation)
                    self.list_annotations.append(a)

            print(self.list_annotations)
            for i in self.list_annotations:
                print(i.__dict__)

            cv2.drawContours(image_original_copy, polygon_result, -1, color, thickness=2)
            alpha = 0.5
            mask = image_temp.astype(bool)
            image_original_copy[mask] = cv2.addWeighted(image_original_copy, alpha, image_temp, 1 - alpha, 0)[mask]

            for i in self.list_annotations:
                x, y, w, h = i.bbox
                cv2.rectangle(image_original_copy, (x, y), (x + w, y + h), (0, 255, 0), 2)
        return image_original_copy, polygon_result

    def unpackArray(self, array):
        # print('=============')
        res = []
        for i in array:
            for j in i:
                a, b = j
                res.append(float(a))
                res.append(float(b))
        return res

    def predict(self, batch, original_image):
        print(f" ==========  {self.objectName()} ========== ")
        self.list_annotations.clear()
        if self.model is not None:

            res = self.model.predict(batch)
            img_original_resize = cv2.resize(original_image, (512, 512), interpolation=cv2.INTER_AREA)
            list_predict = list()
            dd = ['1', '2', '3', '4', '5']
            for i in range(len(res[0, 0, 0, :])):
                r_one = (res[0, :, :, i] > 0.7).astype(np.float32)
                r_one = np.array(r_one)
                list_predict.append(r_one)
            color1 = []
            for i in self.categorical_predict:
                color1.append(literal_eval(i.color))

            for index, j in enumerate(list_predict):
                color = color1[index]
                print(color)
                if np.sum(j) > 5:
                    category = self.categorical_predict[index]
                    print(f'category: {category.name_category_ru} np.sum: {np.sum(j)}')

                    img1, polygon1 = self.drawingMaskForImagePredict(image=img_original_resize,
                                                                     predict=j,
                                                                     color=color[::-1],
                                                                     result_category=category)

                    plt.imshow(img1)
                    plt.show()
                    img_original_resize = img1

            self.result_scan.emit(self.list_annotations)
            #

            # result_mask = []
            # for i in polygon1:
            #     result_mask.append(self.unpackArray(i))
            # base64_polygon = base64.b64encode(str(result_mask).encode())

            # img2, polygon2, area_full2 = self.drawingMaskForImagePredict(image=img1, predict=predict2, color=color2[::-1])
            # img3, polygon3, area_full3 = self.drawingMaskForImagePredict(image=img2, predict=predict3, color=color3[::-1])

            # scan_list = []
            # scan_list: list[ResultScan]
            # if area_full1 != 0:
            #     scan = ResultScan()
            #     scan.color = color
            #     print(max_index)
            #     if max_index <= len(self.categorical_predict):
            #         scan.type_wound = self.categorical_predict[max_index].name_category_ru
            #         scan.result_predict_id = self.categorical_predict[max_index].id_category
            #     else:
            #         scan.type_wound = 'Проверьте категории на сервере'
            #     scan.area_wound = area_full1
            #     scan.polygon_wound = str(base64_polygon)
            #     scan_list.append(scan)

            # if area_full2 != 0:
            #     scan = ResultScan()
            #     scan.color = color2
            #     scan.type_wound = DATASET_LABELS[1]
            #     scan.area_wound = area_full2
            #     scan_list.append(scan)
            #
            # if area_full3 != 0:
            #     scan = ResultScan()
            #     scan.area_wound = area_full3
            #     scan.color = color3
            #     scan.type_wound = DATASET_LABELS[2]
            #     scan_list.append(scan)

            # Заполняем результаты сканирование и передает сигналом в UI

            # scan = ResultScan()

            # scan.polygon_wound = segmentation
            # scan.image_wound = img_original_resize
            # scan.type_wound = DATASET_LABELS[max_index]

            # scan.area_wound

            return img_original_resize

    def image_preprocessing(self, Image_original):

        # train_img = cv2.cvtColor(Image, cv2.IMREAD_ANYDEPTH)
        train_img = cv2.cvtColor(Image_original, cv2.IMREAD_COLOR)
        train_img = cv2.resize(train_img, (128, 128))
        train_img = train_img.astype(np.float32) / 255.

        if (len(train_img.shape) == 3 and train_img.shape[2] == 3):
            pil_image = Image.fromarray((train_img * 255).astype(np.uint8))
            # plt.imshow(pil_image)
            # plt.show()
            return train_img
        else:
            stacked_img = np.stack((train_img,) * 3, axis=-1)
            return stacked_img

    def create_batch(self, image11):
        # image = image11[:, :, 0, :]
        # print(image11.shape)
        from keras.utils import img_to_array
        from tensorflow import expand_dims
        img_array = img_to_array(image11)
        img_array_batch = expand_dims(img_array, 0)  # Create a batch
        return img_array_batch


if __name__ == '__main__':
    l = LoadingModelAndPredict(MODEL_H5_PATH)
    # pred = l.predict()
