def classify_face_shape(landmarks):

    if landmarks is None or len(landmarks) == 0:
        return "unknown"

    # ✅ if mediapipe format
    face_landmarks = landmarks[0]
    points = face_landmarks.landmark

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
