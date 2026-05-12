from face_detection import get_landmarks
from face_shape import classify_face_shape
from recommender import recommend_glasses

import numpy as np
import cv2

def run_pipeline(uploaded_file):
    # 🔥 Convert Streamlit uploaded file → OpenCV image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    # Safety check
    if image is None:
        return {"error": "Invalid image uploaded"}

    # Your pipeline
    landmarks = get_landmarks(image)
    shape = classify_face_shape(landmarks)
    recs = recommend_glasses(shape)

    return {
        "image": image,
        "shape": shape,
        "recommendations": recs
    }