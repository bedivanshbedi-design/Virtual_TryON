from retinaface import RetinaFace

def get_face(image):
    faces = RetinaFace.detect_faces(image)

    if not faces:
        return None

    key = list(faces.keys())[0]
    return faces[key]