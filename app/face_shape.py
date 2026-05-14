def classify_face_shape(face):
    if face is None:
        return "No face detected"

    width = face["right"] - face["left"]
    height = face["bottom"] - face["top"]

    ratio = height / width

    if ratio > 1.5:
        return "Oval"
    elif ratio < 1.2:
        return "Round"
    elif 1.2 <= ratio <= 1.4:
        return "Square"
    else:
        return "Diamond"