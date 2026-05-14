def classify_face_shape(landmarks):
    if landmarks is None:
        return "unknown"

    p = landmarks.landmark

    # Key points
    left_jaw = p[234]
    right_jaw = p[454]

    left_forehead = p[127]
    right_forehead = p[356]

    chin = p[152]
    forehead_top = p[10]

    # Optional: cheekbones (important for accuracy)
    left_cheek = p[50]
    right_cheek = p[280]

    # Measurements
    jaw_width = right_jaw.x - left_jaw.x
    forehead_width = right_forehead.x - left_forehead.x
    cheek_width = right_cheek.x - left_cheek.x
    face_height = chin.y - forehead_top.y

    # Ratios (normalize everything)
    height_ratio = face_height / jaw_width
    forehead_jaw_ratio = forehead_width / jaw_width
    cheek_jaw_ratio = cheek_width / jaw_width

    # ✅ High-sensitivity classification
    if height_ratio > 1.45:
        return "Oval"

    elif cheek_jaw_ratio > 1.08 and cheek_width > forehead_width:
        return "Diamond"

    elif abs(forehead_jaw_ratio - 1.0) < 0.05:
        return "Square"

    elif forehead_jaw_ratio > 1.08:
        return "Heart"

    elif cheek_jaw_ratio > 1.02 and height_ratio < 1.35:
        return "Round"

    else:
        # fallback with subtle decision
        if height_ratio > 1.35:
            return "Oval"
        else:
            return "Round"