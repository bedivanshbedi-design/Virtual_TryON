import numpy as np


def distance(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))


def extract_features(landmarks):

    # Forehead width
    forehead_width = distance(
        landmarks[127],
        landmarks[356]
    )

    # Cheekbone width
    cheekbone_width = distance(
        landmarks[234],
        landmarks[454]
    )

    # Jaw width
    jaw_width = distance(
        landmarks[172],
        landmarks[397]
    )

    # Face height
    face_height = distance(
        landmarks[10],
        landmarks[152]
    )

    features = {
        "forehead_ratio": forehead_width / cheekbone_width,
        "jaw_ratio": jaw_width / cheekbone_width,
        "face_ratio": face_height / cheekbone_width
    }

    return features


def classify_face_shape(landmarks):

    f = extract_features(landmarks)

    forehead = f["forehead_ratio"]
    jaw = f["jaw_ratio"]
    face = f["face_ratio"]

    print(f)

    # ROUND
    if face < 1.25:
        return "Round"

    # OVAL
    elif face >= 1.25 and jaw < 0.85:
        return "Oval"

    # SQUARE
    elif jaw >= 0.85 and forehead > 0.9:
        return "Square"

    # HEART
    elif forehead > jaw:
        return "Heart"

    # DIAMOND
    else:
        return "Diamond"