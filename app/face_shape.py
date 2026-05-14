def classify_face_shape(landmarks, image):
    if landmarks is None:
        return "unknown"

    h_img, w_img, _ = image.shape
    p = landmarks.landmark

    # ✅ STEP 1: Get face bounding box
    xs = [lm.x for lm in p]
    ys = [lm.y for lm in p]

    min_x, max_x = int(min(xs) * w_img), int(max(xs) * w_img)
    min_y, max_y = int(min(ys) * h_img), int(max(ys) * h_img)

    face_w = max_x - min_x
    face_h = max_y - min_y

    if face_w < 50 or face_h < 50:
        return "face too small"

    # ✅ STEP 2: Normalize to face
    def nx(x): return (x * w_img - min_x) / face_w
    def ny(y): return (y * h_img - min_y) / face_h

    # Key features
    jaw = nx(p[454].x) - nx(p[234].x)
    forehead = nx(p[356].x) - nx(p[127].x)
    cheek = nx(p[280].x) - nx(p[50].x)
    height = ny(p[152].y) - ny(p[10].y)

    # ✅ STEP 3: Ratios
    h_ratio = height / jaw
    fw_ratio = forehead / jaw
    cw_ratio = cheek / jaw

    # ✅ DEBUG (remove later if needed)
    print(f"h={h_ratio:.3f}, fw={fw_ratio:.3f}, cw={cw_ratio:.3f}")

    # ✅ STEP 4: Scoring system
    scores = {
        "Oval": 0,
        "Round": 0,
        "Square": 0,
        "Heart": 0,
        "Diamond": 0
    }

    # Oval → taller than wide
    scores["Oval"] += max(0, (h_ratio - 1.3)) * 5

    # Round → shorter face
    scores["Round"] += max(0, (1.3 - h_ratio)) * 5

    # Square → balanced widths
    scores["Square"] += (1 - abs(fw_ratio - 1)) * 3

    # Heart → wider forehead
    scores["Heart"] += max(0, fw_ratio - 1.05) * 4

    # Diamond → wider cheekbones
    scores["Diamond"] += max(0, cw_ratio - 1.05) * 4

    print("Scores:", scores)

    # ✅ STEP 5: Return best match
    return max(scores, key=scores.get)