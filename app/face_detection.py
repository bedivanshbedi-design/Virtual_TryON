import face_recognition

def get_face(image):
    # Detect face locations
    face_locations = face_recognition.face_locations(image)

    if len(face_locations) == 0:
        return None

    top, right, bottom, left = face_locations[0]

    return {
        "top": top,
        "right": right,
        "bottom": bottom,
        "left": left
    }
``