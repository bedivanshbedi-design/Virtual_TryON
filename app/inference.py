from face_detection import get_landmarks
from face_shape import classify_face_shape
from recommender import recommend_glasses

def run_pipeline(uploaded_file):
    image = ... #convert file to cv2 image

    landmarks = get_landmarks(image)
    shape = classify_face_shape(landmarks)
    recs = recommend_glasses(shape)

    return {
        "image": image,
        "shape": shape,
        "recommendations": recs
    }