def classify_face_shape(landmarks):

    if landmarks is None or len(landmarks) == 0:
        return "unknown"

    face_landmarks = landmarks[0]
    points = face_landmarks.landmark

    # DEBUG
    print("Total points:", len(points))  # should be ~468

    # 👉 TEMP logic (just to verify working)
    if len(points) > 400:
        return "oval"
    else:
        return "round"