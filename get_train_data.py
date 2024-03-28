import cv2
import os
class FaceDataCollector:
    def __init__(self, cascade_path='haarcascade_frontalface_default.xml'):
        self.faceCascade = cv2.CascadeClassifier(cascade_path)
        self.cap = cv2.VideoCapture(0)
        self.cap.set(3, 640)  # 设置宽度
        self.cap.set(4, 480)  # 设置高度

    def create_directory(self, directory_name):
        if not os.path.exists(directory_name):
            os.makedirs(directory_name)
    def collect_face_data(self, username):
        print("\n [INFO]准备拍摄，请看着摄像头并等待 ...")
        count = 0  # 记录拍摄了的图像数量

        while True:
            ret, img = self.cap.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # RGB转Gray图形
            faces = self.faceCascade.detectMultiScale(gray, 1.1, 5)

            self.create_directory(f"train data")

            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
                count += 1
                cv2.imwrite(f"train data/User.{username}.{count}.jpg", gray[y:y+h, x:x+w])
                cv2.imshow('image', img)

            k = cv2.waitKey(100) & 0xff   # 按ESC退出
            if k == 27 or count >= 50:   # 拍满50张或按ESC退出
                break

        print("\n [INFO]程序完成，清除无用进程")
        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    face_data_collector = FaceDataCollector()
    user_id = input('\n 输入用户id并回车 ==> ')
    user_name = input('\n 输入用户名并回车')
    face_data_collector.collect_face_data(user_id)