def classify_face_shape(landmarks):
    if landmarks is None or len(landmarks) == 0:
        return "unknown"

    (x, y, w, h) = landmarks[0]

    face_width = w
    face_height = h

    if face_width == 0:
        return "unknown"

    ratio = face_height/face_width

    if ratio > 1.5:
        return "Oval"
    elif 1.2 < ratio <= 1.5:
        return "Heart"
    elif 0.9 < ratio < 1.2:
        return "Round"
    else:
        return "Square"
