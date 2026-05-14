from face_detection import get_landmarks
from face_shape import classify_face_shape
from recommender import recommend_glasses


def run_pipeline(image):

    landmarks = get_landmarks(image)

    if landmarks is None:

        return {
            "image": image,
            "shape": "No face detected",
            "recommendations": []
        }

    shape = classify_face_shape(landmarks)

    recommendations = recommend_glasses(shape)

    return {
        "image": image.copy(),
        "shape": shape,
        "recommendations": recommendations
    }