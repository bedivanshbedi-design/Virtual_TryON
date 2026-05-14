import cv2
from insightface.app import FaceAnalysis

# Initialize model (only once)
app = FaceAnalysis(name="buffalo_l")
app.prepare(ctx_id=0)  # CPU = 0, GPU = 1 (if available)

def get_face(image):
    faces = app.get(image)

    if len(faces) == 0:
        return None

    return faces[0]
