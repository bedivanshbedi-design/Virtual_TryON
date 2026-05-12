import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config.mappings import FACE_SHAPE_MAP

def recommend_glasses(shape):
    return FACE_SHAPE_MAP.get(shape, ["Standard Frame"])