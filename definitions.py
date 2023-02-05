import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))  # This is your Project Root

MODEL_H5_PATH = os.path.join(ROOT_DIR, "model/model3.h5")
DATASET_PATH = os.path.join(ROOT_DIR, "Image_test")

DATASET_LABELS = ['Асептическое', 'Бактериальное', 'Гнойное']

