import cv2
import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh

def get_landmarks(image):
    with mp_face_mesh.FaceMesh(static_image_mode=True) as face_mesh:

        # ✅ Convert BGR → RGB
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        results = face_mesh.process(rgb_image)

        if not results.multi_face_landmarks:
            return None

        return results.multi_face_landmarks