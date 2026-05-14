from mappings import RECOMMENDATION_MAP


def recommend_glasses(face_shape, event):

    # Face shape recommendations
    face_data = RECOMMENDATION_MAP.get(
        face_shape,
        {}
    )

    # Event-specific recommendations
    recommendations = face_data.get(
        event,
        ["Classic Wayfarer"]
    )

    return recommendations