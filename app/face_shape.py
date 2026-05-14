def classify_face_shape(landmarks):
    if landmarks is None:
        return "unknown"

    points = landmarks.landmark

    # Key points
    left_jaw = points[234]
    right_jaw = points[454]

    left_forehead = points[127]
    right_forehead = points[356]

    chin = points[152]
    forehead_top = points[10]

    # Measurements
    jaw_width = right_jaw.x - left_jaw.x
    forehead_width = right_forehead.x - left_forehead.x
    face_height = chin.y - forehead_top.y

    ratio = face_height / jaw_width

    width_diff = abs(jaw_width - forehead_width)

    # Classification
   
   if ratio > 1.35:
        return "Oval"

    elif width_diff < 0.04:
        return "Square"

    elif forehead_width > jaw_width * 1.05:
        return "Heart"

    elif jaw_width > forehead_width * 1.05:
        return "Round"

    else:
        return "Oval"

