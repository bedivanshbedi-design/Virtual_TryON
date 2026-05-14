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
    jaw_width = right_jaw.x - left_jaw.x
    forehead_width = right_forehead.x - left_forehead.x
    cheek_width = right_cheek.x - left_cheek.x
    face_height = chin.y - forehead_top.y

    # Ratios
    height_ratio = face_height / jaw_width
    fw_jaw = forehead_width / jaw_width
    cheek_jaw = cheek_width / jaw_width

    # ✅ DEBUG (important)
    print(f"h:{height_ratio:.2f}, fw:{fw_jaw:.2f}, cheek:{cheek_jaw:.2f}")

    # ✅ PRIORITY ORDER (important)

    # 1. Oval → tall face
    if height_ratio > 1.45:
        return "Oval"

    # 2. Heart → wide forehead, narrow jaw
    if fw_jaw > 1.10:
        return "Heart"

    # 3. Diamond → wide cheekbones
    if cheek_jaw > 1.10:
        return "Diamond"

    # 4. Round → wide face, low height
    if height_ratio < 1.30:
        return "Round"

    # 5. Square → LAST (strict condition)
    if abs(fw_jaw - 1.0) < 0.03 and height_ratio < 1.40:
        return "Square"

    # fallback
    return "Oval"
``