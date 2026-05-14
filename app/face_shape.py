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
    left_cheek = p[50]
    right_cheek = p[280]

    # Measurements
    jaw = right_jaw.x - left_jaw.x
    forehead = right_forehead.x - left_forehead.x
    cheek = right_cheek.x - left_cheek.x
    height = chin.y - forehead_top.y

    # Ratios
    h = height / jaw
    fw = forehead / jaw
    cw = cheek / jaw

    # ✅ Scores (this is the KEY)
    scores = {
        "Oval": 0,
        "Round": 0,
        "Square": 0,
        "Heart": 0,
        "Diamond": 0
    }

    # ✅ Add contributions instead of hard rules

    # Oval → tall face
    scores["Oval"] += max(0, h - 1.3) * 5

    # Round → short + wide
    scores["Round"] += max(0, 1.3 - h) * 5

    # Square → equal widths
    scores["Square"] += max(0, 1 - abs(fw - 1)) * 3

    # Heart → wide forehead
    scores["Heart"] += max(0, fw - 1.05) * 4

    # Diamond → wide cheekbones
    scores["Diamond"] += max(0, cw - 1.05) * 4

    # ✅ Debug (VERY useful)
    print("Ratios:", f"h={h:.2f}, fw={fw:.2f}, cw={cw:.2f}")
    print("Scores:", scores)

    # ✅ Return best match
    return max(scores, key=scores.get)
