import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))  # This is your Project Root

MODEL_H5_PATH = os.path.join(ROOT_DIR, "unet_model/model3.h5")
DATASET_PATH = os.path.join(ROOT_DIR, "Image_test")
EXE = os.path.join(ROOT_DIR, "main.exe")
EXE_NEW = os.path.join(ROOT_DIR, "main_OLD.exe")
ZIP_FILE_NEW = os.path.join(ROOT_DIR, "update.zip")

DATASET_LABELS = ['Асептическое', 'Бактериальное', 'Гнойное']

DEBUG_MODE = False

