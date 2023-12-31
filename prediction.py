from ultralytics import YOLO
from ultralytics.models.yolo.detect.predict import DetectionPredictor
import imageio.v3 as iio
import cv2

def model_train():
    model = YOLO('./runs/classify/train/weights/best.pt')
    model.fuse()
    return model

def conver_to_img(fileUploaded):
    return iio.imread(fileUploaded)

def predict_image(file_path):
    model_data = model_train()
    result = model_data(file_path)
    print(result)
    return result[0].names[result[0].probs.top1]

def predict_cap():
    model_data = model_train()
    result = model_data.predict(source="0", show=True, conf=0.5)
    print(result[0].names[result[0].probs.top1])