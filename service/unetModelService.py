import time
from ast import literal_eval

import cv2
import numpy as np
import tensorflow as tf
from PIL import Image
from PySide6.QtCore import QThread, Signal
from PySide6.QtCore import Qt
from PySide6.QtGui import QImage, QPixmap

from model.Annotations import Annotations
from model.result_predict import ResultPredict


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
            predict = self.predict(image)
            image_qt = self.opencvFormatToQImage(predict)
            self.predict_image_result.emit(QPixmap.fromImage(image_qt))
        else:
            self.video_stream_image.emit(QImage())
        print('Поток закончил свою работу')

    def load_model_func(self):
        # iou1111 = MyMeanIOU(num_classes=12)
        if self.model is None:
            print(self.path_model)
            interpreter = tf.lite.Interpreter(model_path=self.path_model)
            interpreter.allocate_tensors()
            print('------ Загружаю модель ------')
            self.model = interpreter

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
        # print(color)
        print(result_category.name_category_ru)
        p = cv2.resize(predict, (512, 512), interpolation=cv2.INTER_AREA)
        p = p.astype('uint8')
        polygon, hierarchy = cv2.findContours(p, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        # print(polygon)
        image_original_copy = image.copy()
        polygon_result = []
        if polygon is not None:

            # print(dir(polygon))
            polygon = sorted(polygon, key=cv2.contourArea, reverse=True)
            image_temp = np.zeros_like(image, np.uint8)
            image_original_copy = image.copy()
            print(f'count polygon: {len(polygon)}')

            for contour in polygon:
                # print(contour)
                peri = cv2.arcLength(contour, True)
                if peri > 100:
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
                    a.result_predict = result_category
                    a.area = cv2.contourArea(polygon_annotation)
                    self.list_annotations.append(a)

            # print(self.list_annotations)
            # for i in self.list_annotations:
            #     print(i.__dict__)

            cv2.drawContours(image_original_copy, polygon_result, -1, color, thickness=2)
            alpha = 0.5
            mask = image_temp.astype(bool)
            image_original_copy[mask] = cv2.addWeighted(image_original_copy, alpha, image_temp, 1 - alpha, 0)[mask]

            for i in self.list_annotations:
                x, y, w, h = i.bbox
                # cv2.rectangle(image_original_copy, (x, y), (x + w, y + h), color, 2)
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

    def predict(self, original_image):
        print(f" ==========  {self.objectName()} ========== ")
        print(f" ==========  {np.array(original_image).shape} ========== ")
        self.list_annotations.clear()
        if self.model is not None:

            start = time.time()  ## точка отсчета времени

            # Получение входного и выходного тензоров
            input_details = self.model.get_input_details()
            output_details = self.model.get_output_details()

            # Подача изображения на вход модели
            list_predict = list()
            # print(batch.shape)
            image_preprocessing = self.image_preprocessing(original_image, target_shape=input_details[0]['shape'])
            batch_image = self.create_batch(image_preprocessing)
            # return 0
            self.model.set_tensor(input_details[0]['index'], batch_image)
            img_original_resize = cv2.resize(original_image, (512, 512), interpolation=cv2.INTER_AREA)
            # Выполнение предсказания
            self.model.invoke()
            # Получение результата предсказания
            print('output tensor: ' + str(output_details[0]['index']))

            end = time.time() - start  ## собственно время работы программы
            print(f'время распознавания: {end}')  ## вывод времени

            result_predict = self.model.get_tensor(output_details[0]['index'])  # Получаю тензор 1 256 256 4
            result_predict = np.squeeze(result_predict)  # Убираю 1, получается тензор 256, 256,3
            result_predict = tf.nn.softmax(result_predict,
                                           axis=-1)  # Сглаживаю значения что бы вероятности были в диапазоне от 0 до 1

            argmax_predict = np.argmax(np.array(result_predict),
                                       axis=-1)  # получаю максимальное значение по последней оси
            result_predict = tf.keras.utils.to_categorical(
                argmax_predict)  # Разворачиваю массив в размерность, сколько нашлось категорий+1
            result_predict = result_predict[:, :, 1:]  # Убираю фон на распознанном изображении

            for i in range(len(result_predict[0, 0, :])):
                r_one = result_predict[:, :, i]
                r_one = np.array(r_one)
                list_predict.append(r_one)
            color1 = []
            for i in self.categorical_predict:
                color1.append(literal_eval(i.color))

            for index, j in enumerate(list_predict):
                color = color1[index]
                # print(color)
                if np.sum(j) > 100:
                    category = self.categorical_predict[index]
                    print(f'category: {category.name_category_ru} np.sum: {np.sum(j)}')

                    img1, polygon1 = self.drawingMaskForImagePredict(image=img_original_resize,
                                                                     predict=(j * 255).astype(np.uint8),
                                                                     color=color[::-1],
                                                                     result_category=category)

                    img_original_resize = img1

            self.result_scan.emit(self.list_annotations)

            return img_original_resize

    def image_preprocessing(self, Image_original, target_shape=(1, 256, 256, 3)):

        # train_img = cv2.cvtColor(Image, cv2.IMREAD_ANYDEPTH)
        print(f'target_shape: {target_shape}')
        train_img = cv2.cvtColor(Image_original, cv2.COLOR_BGR2RGB)
        train_img = cv2.resize(train_img, (target_shape[1], target_shape[2]))
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
        img_array = img_to_array(image11 * 255)
        img_array_batch = expand_dims(img_array, 0)  # Create a batch
        return img_array_batch


if __name__ == '__main__':
    pass

    # l = LoadingModelAndPredict(MODEL_H5_PATH)
    # pred = l.predict()
