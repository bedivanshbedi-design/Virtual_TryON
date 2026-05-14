import cv2
import mediapipe as mp
print("MediaPipe imported successfully")

mp_face_mesh = mp.solutions.face_mesh


def get_landmarks(image):
    with mp_face_mesh.FaceMesh(static_image_mode=True) as face_mesh:
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(rgb)

        if not results.multi_face_landmarks:
            return None
        
        return results.multi_face_landmarks[0]


