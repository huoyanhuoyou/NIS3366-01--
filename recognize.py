import time  # 导入时间模块
import os
import cv2

class FaceRecognizer:
    def __init__(self, trainer_path="trainer/trainer.yml"):
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.recognizer.read(trainer_path)
        self.faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.save_dir = "failed_logins"  # 保存失败登录照片的目录
        if not os.path.exists(self.save_dir):
            os.makedirs(self.save_dir)

        self.cooldown_time = 5  # 冷却时间为60秒
        self.last_failed_login_time = 0  # 上次失败登录时间初始化为0

    def save_failed_login_image(self, image):
        img_name = f"failed_login_{len(os.listdir(self.save_dir)) + 1}.jpg"
        cv2.imwrite(os.path.join(self.save_dir, img_name), image)

    def recognize_faces(self, username):
        cam = cv2.VideoCapture(0)
        cam.set(3, 640)  # 设置宽度
        cam.set(4, 480)  # 设置高度
        minW = 0.1 * cam.get(3)
        minH = 0.1 * cam.get(4)

        while True:
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = self.faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.2,
                minNeighbors=5,
                minSize=(int(minW), int(minH)),
            )

            for (x, y, w, h) in faces:
                id, confidence = self.recognizer.predict(gray[y:y + h, x:x + w])

                # 优先使用用户名进行识别
                if username == str(id) and confidence > 50:
                    # 允许通过
                    cv2.putText(img, f"Welcome, {username}!", (x, y - 20), self.font, 1, (0, 255, 0), 2)
                    cam.release()
                    cv2.destroyAllWindows()
                    print("您的身份已核实：", id)
                    return True
                else:
                    # 检查冷却时间是否已过
                    current_time = time.time()
                    if current_time - self.last_failed_login_time >= self.cooldown_time:
                        # 保存失败登录照片
                        self.save_failed_login_image(img)
                        self.last_failed_login_time = current_time  # 更新上次失败登录时间

                        # 输出错误
                        cv2.putText(img, "Access Denied!", (x, y - 20), self.font, 1, (0, 0, 255), 2)

                # 显示识别信息
                cv2.putText(img, f"ID: {id}", (x + 5, y - 5), self.font, 1, (255, 255, 0), 2)
                cv2.putText(img, f"Confidence: {round(100 - confidence)}%", (x + 5, y + h - 5), self.font, 1,
                            (255, 255, 0), 2)

            cv2.imshow('FaceRecognition', img)

            k = cv2.waitKey(10) & 0xff
            if k == 27:  # ESC键退出
                break

        cam.release()
        cv2.destroyAllWindows()
        return False


# 使用示例
if __name__ == "__main__":
    # 假设前端传入的用户名为 username
    username = input("Please enter your username: ")
    face_recognizer = FaceRecognizer()
    face_recognizer.recognize_faces(username)