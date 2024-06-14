import cv2
from deepface import DeepFace
import time


def config_list(em_list):
    items_to_remove = ['neutral', 'surprise', 'disgust', 'fear']
    em_list = [em for em in em_list if em not in items_to_remove]
    if len(em_list) == 0:
        return -1
    return max(set(em_list), key=em_list.count)


def find_emotion():
    cap = cv2.VideoCapture(0)
    start_time = time.time()
    emotion_list = []
    while cap.isOpened():
        ret, frame = cap.read()

        face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 5)

        try:
            result = DeepFace.analyze(img_path=frame, actions=['emotion'])
            emotion = result[0]['dominant_emotion']
            emotion_list.append(emotion)
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        except:
            cv2.putText(frame, "no face recognized", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        cv2.imshow('Moodtune', frame)
        if cv2.waitKey(1) & 0xff == ord('q'):  #change keys
            break
        time_difference = int(time.time() - start_time)
        if time_difference > 15:
            break
    cap.release()
    cv2.destroyAllWindows()
    return config_list(emotion_list)
