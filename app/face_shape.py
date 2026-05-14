import numpy as np


def distance(p1, p2):

    return np.linalg.norm(
        np.array(p1) - np.array(p2)
    )


def classify_face_shape(landmarks):

    # -------------------------
    # IMPORTANT LANDMARKS
    # -------------------------

    forehead_left = landmarks[54]
    forehead_right = landmarks[284]

    cheek_left = landmarks[234]
    cheek_right = landmarks[454]

    jaw_left = landmarks[172]
    jaw_right = landmarks[397]

    chin = landmarks[152]
    forehead_top = landmarks[10]

    # -------------------------
    # DISTANCES
    # -------------------------

    forehead_width = distance(
        forehead_left,
        forehead_right
    )

    cheekbone_width = distance(
        cheek_left,
        cheek_right
    )

    jaw_width = distance(
        jaw_left,
        jaw_right
    )

    face_length = distance(
        forehead_top,
        chin
    )

    # -------------------------
    # NORMALIZED RATIOS
    # -------------------------

    face_ratio = face_length / cheekbone_width

    jaw_ratio = jaw_width / cheekbone_width

    forehead_ratio = forehead_width / cheekbone_width

    # -------------------------
    # CLASSIFICATION
    # -------------------------

    # ROUND
    if (
        face_ratio < 1.28 and
        jaw_ratio > 0.83
    ):

        detected_shape = "Round"

    # OVAL
    elif (
        face_ratio >= 1.33 and
        jaw_ratio < 0.83
    ):

        detected_shape = "Oval"

    # SQUARE
    elif (
        jaw_ratio >= 0.85 and
        forehead_ratio >= 0.90
    ):

        detected_shape = "Square"

    # HEART
    elif (
        forehead_ratio > jaw_ratio and
        jaw_ratio < 0.80
    ):

        detected_shape = "Heart"

    # DIAMOND
    else:

        detected_shape = "Diamond"

    # -------------------------
    # DEBUG VALUES
    # -------------------------

    print({
        "shape": detected_shape,
        "face_ratio": round(face_ratio, 2),
        "jaw_ratio": round(jaw_ratio, 2),
        "forehead_ratio": round(forehead_ratio, 2)
    })

    # -------------------------
    # RETURN DICTIONARY
    # -------------------------

    return {
        "shape": detected_shape,
        "face_ratio": round(face_ratio, 2),
        "jaw_ratio": round(jaw_ratio, 2),
        "forehead_ratio": round(forehead_ratio, 2)
    }