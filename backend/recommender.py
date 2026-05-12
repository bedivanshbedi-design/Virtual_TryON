import sys
import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT_DIR)
from config.mappings import FACE_SHAPE_MAP

def recommend_glasses(shape):
    return FACE_SHAPE_MAP.get(shape, ["Standard Frame"])