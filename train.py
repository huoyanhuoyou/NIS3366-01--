import os
import cv2
import numpy as np
from PIL import Image

class FaceRecognize_trainer:
    def __init__(self, train_data_path, classifier_path="haarcascade_frontalface_default.xml"):
        self.train_data_path = train_data_path
        self.recognizer = cv2.face.LBPHFaceRecognizer.create()
        self.detector = cv2.CascadeClassifier(classifier_path)

    def get_images_and_labels(self):
        image_paths = [os.path.join(self.train_data_path, f) for f in os.listdir(self.train_data_path)]
        face_samples = []
        ids = []
        for image_path in image_paths:
            PIL_img = Image.open(image_path).convert('L')  # 转换成灰度模式
            img_numpy = np.array(PIL_img, 'uint8')  # 将图片转化为numpy数组
            id = int(os.path.split(image_path)[-1].split(".")[1])
            faces = self.detector.detectMultiScale(img_numpy)
            for (x, y, w, h) in faces:
                face_samples.append(img_numpy[y:y+h, x:x+w])
                ids.append(id)
        return face_samples, ids

    def create_directory(self, directory_name):
        if not os.path.exists(directory_name):
            os.makedirs(directory_name)
    def train(self):
        print("\n [INFO] 正在训练模型 ...")
        faces, ids = self.get_images_and_labels()
        self.recognizer.train(faces, np.array(ids))  # 训练
        self.create_directory("trainer")
        self.recognizer.write('trainer/trainer.yml')  # 保存模型到 trainer.yml
        print("\n [INFO] {0} 成功训练，正在退出程序".format(len(np.unique(ids))))

# 使用示例
if __name__ == "__main__":
    # 假设你的训练图片存放在"train data"目录下
    face_recognizer = FaceRecognizer("train data")
    face_recognizer.train()