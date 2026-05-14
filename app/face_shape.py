import numpy as np

def classify_face_shape(face, image):
    if face is None:
        return "No face detected"

    # ✅ Get bounding box
    x1, y1, x2, y2 = face.bbox.astype(int)

    face_crop = image[y1:y2, x1:x2]

    if face_crop.size == 0:
        return "Face crop error"

    h, w, _ = face_crop.shape

    # ✅ Basic ratios (strong baseline)
    aspect_ratio = h / w

    # ✅ Get keypoints (eyes, nose, mouth corners)
    kps = face.kps  # shape: (5, 2)

    left_eye, right_eye, nose, left_mouth, right_mouth = kps

    # ✅ Feature distances
    eye_width = np.linalg.norm(left_eye - right_eye)
    mouth_width = np.linalg.norm(left_mouth - right_mouth)

    # Normalize by face width
    eye_ratio = eye_width / w
    mouth_ratio = mouth_width / w

    # ✅ DEBUG (important)
    print(f"""
    aspect_ratio: {aspect_ratio:.2f}
    eye_ratio: {eye_ratio:.2f}
    mouth_ratio: {mouth_ratio:.2f}
    """)

    # ✅ Classification logic (much more stable)

    if aspect_ratio > 1.5:
        return "Oval"

    if aspect_ratio < 1.2:
        return "Round"

    if eye_ratio > 0.35:
        return "Square"

    if mouth_ratio < 0.25:
        return "Heart"

    return "Diamond"
``