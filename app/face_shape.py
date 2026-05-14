def classify_face_shape(landmarks):
    if landmarks is None:
        return "unknown"

    p = landmarks.landmark

    # Points
    jaw = p[454].x - p[234].x
    forehead = p[356].x - p[127].x
    cheek = p[280].x - p[50].x
    height = p[152].y - p[10].y

    # Normalize
    h = height / jaw
    fw = forehead / jaw
    cw = cheek / jaw

    # 🔥 amplify differences
    h_score = (h - 1.3) * 10
    fw_score = (fw - 1.0) * 10
    cw_score = (cw - 1.0) * 10

    print("DEBUG:", h_score, fw_score, cw_score)

    # Decision
    if h_score > 1.5:
        return "Oval"

    if fw_score > 1.5:
        return "Heart"

    if cw_score > 1.5:
        return "Diamond"

    if h_score < -1.0:
        return "Round"

    return "Square"
