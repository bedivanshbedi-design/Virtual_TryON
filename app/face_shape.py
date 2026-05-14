def classify_face_shape(landmarks):
    if landmarks is None:
        return "unknown"

    points = landmarks.landmark

    # Key points
    left_jaw = points[234].x
    right_jaw = points[454].x

    left_forehead = points[127].x
    right_forehead = points[356].x

    chin = points[152].y
    forehead_top = points[10].y

    # Measurements
    jaw_width = right_jaw - left_jaw
    forehead_width = right_forehead - left_forehead
    face_height = chin - forehead_top

    ratio = face_height / jaw_width

    # Classification
    if abs(jaw_width - forehead_width) < 0.02:
        if ratio < 1.2:
            return "Square"
        else:
            return "Oval"
    elif forehead_width > jaw_width:
        return "Heart"
    else:
        return "Round"
