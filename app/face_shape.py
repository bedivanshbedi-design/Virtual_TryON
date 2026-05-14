import numpy as np

# ✅ Pre-defined reference vectors (dummy for now)
# In real case, you should compute from real dataset
FACE_SHAPE_REFERENCES = {
    "Oval": np.random.rand(512),
    "Round": np.random.rand(512),
    "Square": np.random.rand(512),
    "Heart": np.random.rand(512),
    "Diamond": np.random.rand(512)
}

def classify_face_shape(face):
    if face is None:
        return "No face detected"

    embedding = face.embedding  # ✅ THIS IS THE KEY

    best_match = None
    best_score = float("inf")

    for shape, ref in FACE_SHAPE_REFERENCES.items():
        dist = np.linalg.norm(embedding - ref)

        if dist < best_score:
            best_score = dist
            best_match = shape

    return best_match