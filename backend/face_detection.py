import cv2
import mediapipe as mp 

mp_face_mesh = mp.solutions.face_mesh 
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=True)

def get_landmarks(image):
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb)

    if results.multi_face_landmarks:
        return results.multi_face_landmarks[0]
    return none