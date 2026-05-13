def classify_face_shape(landmarks):
    if landmarks is None or len(landmarks) == 0:
        return "unknown"

    (x, y, w, h) = landmarks[0]

    face_width = int(w*0.85)
    face_height = int(h*0.9)

    if face_width == 0:
        return "unknown"

    ratio = face_height/face_width

    if ratio > 1.4:
        return "Oval"
    elif 1.15 < ratio <= 1.4:
        return "Heart"
    elif 0.95 < ratio < 1.15:
        return "Round"
    else:
        return "Square"
