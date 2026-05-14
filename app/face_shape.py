def classify_face_shape(face):
    if face is None:
        return "No face detected"

    x1, y1, x2, y2 = face["facial_area"]
    width = x2 - x1
    height = y2 - y1

    ratio = height / width

    if ratio > 1.5:
        return "Oval"
    elif ratio < 1.2:
        return "Round"
    elif 1.2 <= ratio <= 1.4:
        return "Square"
    else:
        return "Diamond"
``