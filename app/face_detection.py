from insightface.app import FaceAnalysis

app = FaceAnalysis()
app.prepare(ctx_id=0)

def get_face(image):
    faces = app.get(image)
    return faces[0] if len(faces) > 0 else None
