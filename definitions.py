import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))  # This is your Project Root

MODEL_H5_PATH = os.path.join(ROOT_DIR, "unet_model/model_1_0_10.h5")
DATASET_PATH = os.path.join(ROOT_DIR, "Image_test")
