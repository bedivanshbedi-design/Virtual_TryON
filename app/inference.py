from face_detection import get_landmarks
from face_shape import classify_face_shape
from recommender import recommend_glasses
from event_nlp import detect_event

def run_pipeline(image, user_text):

    landmarks = get_landmarks(image)

    if landmarks is None:

        return {
            "shape": "No face detected",
            "event": "Unknown",
            "recommendations": []
        }

    face_result= classify_face_shape(landmarks)

    face_shape= face_result["shape"]

    event_result= detect_event(user_text)

    detected_event = event_result["event"]



    recommendations = recommend_glasses(face_shape,detected_event )

    return {
        "shape": face_shape,
        "recommendations": recommendations,
        "event": detected_event,
        "event_confidence": event_result["confidence"]
        "metrics": face_result
    }

