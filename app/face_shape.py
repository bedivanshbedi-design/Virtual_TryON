def classify_face_shape(landmarks):
    if not landmarks:
        return "unknown"

    face = landmarks[0]

    points = face.landmark

    face_width = abs(points[234].x - points[454].x)
    face_height = abs(points[10].x - points[152].x)

    ratio = face_height/face_width

    if ratio > 1.5:
        return "Oval"
    elif 1.2 < ratio <= 1.5:
        return "Heart"
    elif 0.9 < ratio < 1.2:
        return "Round"
    else:
        return "Square"
