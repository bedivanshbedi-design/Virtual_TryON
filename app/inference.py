from face_detection import get_landmarks
from face_shape import classify_face_shape
from recommender import recommend_glasses

import numpy as np 
import os

def load_image(uploaded_file):
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    return image


def run_pipeline(uploaded_file):
    image = load_image(uploaded_file)

    landmarks = get_landmarks(image)
    shape = classify_face_shape(landmarks)
    recs = recommend_glasses(shape)

    return {
        "image": image,
        "shape": shape,
        "recommendations": recs
    }