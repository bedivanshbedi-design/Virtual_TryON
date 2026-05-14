import cv2
import mediapipe as mediapipe

mp_face_mesh = mp.solutions.mp_face_mesh

# Load pre-trained Haar cascade
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

def get_landmarks(image):
    with mp_face_mesh.FaceMesh(static_image_mode=True) as face_mesh:
        rgb = cv2.cvtCOlor(image, cv2.COLOR_BGR2BGR)
        results = face_mesh.multi_face_landmarks:

        if not results.multi_face_landmarks:
            return None
        
        return results.multi_face_landmarks[0]


