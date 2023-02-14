import os
import random
import time

import cv2
import numpy as np
from PIL import Image
from PySide6.QtCore import QThread, Signal
from PySide6.QtCore import Qt
from PySide6.QtGui import QImage
from matplotlib import pyplot as plt
from definitions import DATASET_PATH, MODEL_H5_PATH, DATASET_LABELS
from model.result_scan import ResultScan


class LoadingModelAndPredict(QThread):
    loading_model_end = Signal(str)
    predict_image_result = Signal(QImage)
    image_original = Signal(QImage)
    result_scan = Signal(ResultScan)
    # Запомнить номер камеры
    number_cam = -1
    play_video = True

    def __init__(self, path_model, parent=None):
        super(LoadingModelAndPredict, self).__init__(parent)
        start = time.time()
        self.model = None
        self.path_model = path_model
        # self.model: Model
        self.segmentation_polygon = None
        self.area = None
        self.image_batch = None
        self.scan_from_cam = False
        self.image_path = None
        print('1')
        end_time = time.time() - start
        print(end_time)

    def set_image_path(self, path_image):
        self.image_path = path_image

    def opencvFormatToQImage(self, image: QImage):
        # print(image)
        convertToQtFormats = QImage(image.data, image.shape[1], image.shape[0],
                                    QImage.Format.Format_BGR888)
        qimage = convertToQtFormats.scaled(512, 512, Qt.KeepAspectRatio)
        return qimage
    def video_stream(self):
        print('streamVideo')
        print(self.play_video)
        cap = cv2.VideoCapture(self.number_cam, cv2.CAP_DSHOW)
        while True:
            if self.play_video:
                print('222222')
                ret, frame = cap.read()
                self.image_original.emit(self.opencvFormatToQImage(frame))
            else:
                cap.release()
                cv2.destroyAllWindows()
                print('поток закончен')
                break

    def run(self):
        self.video_stream()
        print('==========___==========')
        image = self.get_image()
        self.image_original.emit(self.opencvFormatToQImage(image))
        print('Началась загрузка модели в отдельном потоке')
        secundomer = time.time()
        self.load_model_func()
        res = round(time.time() - secundomer, 2)
        self.loading_model_end.emit(str(res))  # посылаем сигнал с временем загрузки модели
        image_preprocessing = self.image_preprocessing(image)
        batch_image = self.create_batch(image_preprocessing)
        predict = self.predict(batch_image, image)
        image_qt = self.opencvFormatToQImage(predict)
        self.predict_image_result.emit(image_qt)
        print('Поток закончил свою работу')

    def load_model_func(self):
        from keras.models import load_model
        from utils.unet_model.model_losses import dice_coef, bce_dice_loss
        if self.model is None:
            print('------ Загружаю модель ------')
            self.model = load_model(self.path_model,
                                    custom_objects={'dice_coef': dice_coef,
                                                    'bce_dice_loss': bce_dice_loss})
            return self.model
        else:
            return self.model

    def get_image(self):
        # Получение картинки с камеры
        if self.scan_from_cam and self.image_path is None:
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
            # Получаем картинку если картинка из каталога
            image = cv2.imread(self.image_path, cv2.COLOR_BGR2RGB)
            return image

    def drawingMaskForImagePredict(self, image: Image, predict: Image, color):
        p = cv2.resize(predict, (512, 512), interpolation=cv2.INTER_AREA)
        dilation = cv2.dilate(p, (3, 3), iterations=1)
        edged = cv2.Canny(dilation, 1, 200)
        polygon, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        # print(polygon)
        image_original_copy = image.copy()
        area_full = 0
        if polygon is not None:
            # print(dir(polygon))
            polygon = sorted(polygon, key=cv2.contourArea, reverse=True)
            image_temp = np.zeros_like(image, np.uint8)
            image_original_copy = image.copy()
            print(image_temp.shape)
            for contour in polygon:
                area_full += cv2.contourArea(contour)
                cv2.fillPoly(image_temp, pts=[contour], color=color)
                # contour = contour.flatten().tolist()
                # if len(contour) > 4:
                #     segmentation.append(contour)
            cv2.drawContours(image_original_copy, polygon, -1, color, thickness=2)
            alpha = 0.5
            mask = image_temp.astype(bool)
            image_original_copy[mask] = cv2.addWeighted(image_original_copy, alpha, image_temp, 1 - alpha, 0)[mask]
        return image_original_copy, polygon, area_full

    def predict(self, batch, original_image):
        print(f" ==========  {self.objectName()} ========== ")

        if self.model is not None:
            res = self.model.predict(batch)
            img_original_resize = cv2.resize(original_image, (512, 512), interpolation=cv2.INTER_AREA)

            list_predict = list()
            list_predict.append(np.sum(res[0, :, :, 0]))
            list_predict.append(np.sum(res[0, :, :, 1]))
            list_predict.append(np.sum(res[0, :, :, 2]))
            max_value = max(list_predict)
            max_index = list_predict.index(max_value)

            predict1 = res[0, :, :, max_index]
            predict1 = (predict1 > 0.4).astype(np.uint8)
            predict1 = np.array(predict1) * 255

            predict2 = res[0, :, :, 1]
            predict2 = (predict2 > 0.4).astype(np.uint8)
            predict2 = np.array(predict2) * 255

            predict3 = res[0, :, :, 2]
            predict3 = (predict3 > 0.4).astype(np.uint8)
            predict3 = np.array(predict3) * 255

            color1 = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
            color = color1[max_index]
            # color2 = (0, 255, 0)
            # color3 = (0, 0, 255)

            # Расширение
            img1, polygon1, area_full1 = self.drawingMaskForImagePredict(image=img_original_resize, predict=predict1,
                                                                         color=color[::-1])

            # img2, polygon2, area_full2 = self.drawingMaskForImagePredict(image=img1, predict=predict2, color=color2[::-1])
            # img3, polygon3, area_full3 = self.drawingMaskForImagePredict(image=img2, predict=predict3, color=color3[::-1])

            scan_list = []
            scan_list: list[ResultScan]
            if area_full1 != 0:
                scan = ResultScan()
                scan.color = color
                scan.type_wound = DATASET_LABELS[max_index]
                scan.area_wound = area_full1
                scan_list.append(scan)

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

            self.result_scan.emit(scan_list)

            # scan.area_wound

            return img1

    def get_random_image(self):
        image_path = os.path.join(DATASET_PATH, random.choice(os.listdir(DATASET_PATH)))
        return image_path

    def image_preprocessing(self, Image_original):

        # train_img = cv2.cvtColor(Image, cv2.IMREAD_ANYDEPTH)
        train_img = cv2.cvtColor(Image_original, cv2.IMREAD_COLOR)
        train_img = cv2.resize(train_img, (128, 128))
        train_img = train_img.astype(np.float32) / 255.

        if (len(train_img.shape) == 3 and train_img.shape[2] == 3):
            print('1')
            pil_image = Image.fromarray((train_img * 255).astype(np.uint8))
            plt.imshow(pil_image)
            plt.show()
            return train_img
        else:
            stacked_img = np.stack((train_img,) * 3, axis=-1)
            print('2')
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
