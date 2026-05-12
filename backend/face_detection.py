import cv2

# Load pre-trained Haar cascade
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

def get_landmarks(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    landmarks = []
    for (x, y, w, h) in faces:
        landmarks.append((x, y, w, h))

    return landmarks