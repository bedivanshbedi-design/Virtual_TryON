def classify_face_shape(landmarks):
    if landmarks is None:
        return "unknown"

    points = landmarks.landmarks

    face_width = abs(point[234].x - points[454].x)
    face_height = abs(points[10].y - points[152].y)

    ratio = face_height / face_width

    if ratio > 1.5:
        return "Oval"
    elif 1.2 < ratio <= 1.5:
        return "Heart"
    elif 0.9 < ratio < 1.2:
        return "Round"
    else:
        return "Square"
