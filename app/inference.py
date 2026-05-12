from face_detection import get_landmarks
from face_shape import classify_face_shape
from recommender import recommend_glasses

import numpy as np
import cv2

def run_pipeline(uploaded_file):
    import numpy as np
    import cv2

    file_bytes = np.frombuffer(uploaded_file.read(), np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    if image is None:
        return {"error": "Invalid image"}

    landmarks = get_landmarks(image)
    
    print("LANDMARKS:", landmarks)

    # 🔥 FIX: handle no face detected
    if landmarks is None:
        return {"error": "No face detected. Please upload a clear front-face image."}

    shape = classify_face_shape(landmarks)
    recs = recommend_glasses(shape)

    return {
        "image": image,
        "shape": shape,
        "recommendations": recs
    }