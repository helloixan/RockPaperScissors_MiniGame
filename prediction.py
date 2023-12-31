from ultralytics import YOLO
import imageio.v3 as iio

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