import os
import numpy as np
import cv2
from insightface.app import FaceAnalysis

app = FaceAnalysis()
app.prepare(ctx_id=0)

DATASET_PATH = "dataset"

FACE_SHAPE_REFERENCES = {}

for shape in os.listdir(DATASET_PATH):
    folder = os.path.join(DATASET_PATH, shape)

    embeddings = []

    for img_name in os.listdir(folder):
        img_path = os.path.join(folder, img_name)
        img = cv2.imread(img_path)

        faces = app.get(img)

        if len(faces) > 0:
            embeddings.append(faces[0].embedding)

    if embeddings:
        FACE_SHAPE_REFERENCES[shape] = np.mean(embeddings, axis=0)

# ✅ Save embeddings
np.save("face_embeddings.npy", FACE_SHAPE_REFERENCES)
print("Saved embeddings ✅")
