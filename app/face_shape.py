def classify_face_shape(landmarks):
    if landmarks is None or len(landmarks) == 0:
        return "unknown"

    (x, y, w, h) = landmarks[0]

    face_width = w*1.1
    face_height = h*0.9

    if face_width == 0:
        return "unknown"

    ratio = face_height/face_width

    if ratio > 1.35:
        return "Oval"
    elif 1.15 < ratio <= 1.35:
        return "Heart"
    elif 0.95 < ratio < 1.15:
        return "Round"
    else:
        return "Square"
