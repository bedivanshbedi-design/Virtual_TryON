from config.mappings import FACE_SHAPE_MAP

def recommend_glasses(shape):
    return FACE_SHAPE_MAP.get(shape, ["Standard Frame"])