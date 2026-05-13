import cv2

# Load pre-trained Haar cascade
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

def get_landmarks(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=6,
        minSize=(30,30)
        )

    if len(faces) == 0:
        return None

    faces = sorted(faces, key = lambda x: x[2]*x[3], reverse=True)
    
    landmarks = []

    for (x, y, w, h) in faces:
        landmarks.append((x, y, w, h))

    return landmarks

