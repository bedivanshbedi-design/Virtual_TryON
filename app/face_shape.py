import numpy as np

def classify_face_shape(landmarks, image):
    if landmarks is None:
        return "No face detected"

    p = landmarks.landmark

    # ✅ Distance function (important improvement)
    def dist(a, b):
        return np.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)

    # ✅ Core measurements
    jaw = dist(p[234], p[454])
    forehead = dist(p[127], p[356])
    cheek = dist(p[50], p[280])
    height = dist(p[10], p[152])

    # ✅ Advanced geometry (key improvement)
    jaw_curve = dist(p[234], p[152]) + dist(p[454], p[152])
    cheek_prominence = cheek - jaw
    forehead_dominance = forehead - jaw

    # ✅ Normalize
    h = height / jaw
    fw = forehead / jaw
    jp = cheek_prominence
    fd = forehead_dominance
    jc = jaw_curve / jaw

    # ✅ DEBUG (VERY IMPORTANT – keep this for now)
    print(f"""
    height_ratio: {h:.3f}
    forehead_ratio: {fw:.3f}
    cheek_prominence: {jp:.4f}
    forehead_dominance: {fd:.4f}
    jaw_curve: {jc:.3f}
    """)

    # ✅ ✅ Final classification logic (robust ordering)

    # Long face → Oval
    if h > 1.45:
        return "Oval"

    # Wide forehead
    if fd > 0.015:
        return "Heart"

    # Wide cheekbones
    if jp > 0.015:
        return "Diamond"

    # Short height
    if h < 1.25:
        return "Round"

    # Flat / angular jaw
    if jc < 2.15:
        return "Square"

    return "Oval"