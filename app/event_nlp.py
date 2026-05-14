from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

EVENTS = [
    "wedding",
    "office",
    "college",
    "party",
    "date",
    "travel",
    "interview",
    "casual"
]

EVENT_EMBEDDINGS = model.encode(EVENTS)

def detect_event(user_text):

    if not user_text:
        return "casual"

    query_embedding = model.encode([user_text])

    similarity = cosine_similarity(
        query_embedding,
        EVENT_EMBEDDINGS
    )

    best_index = np.argmax(similarity)

    detected_event = EVENTS[best_index]

    confidence = similarity[0][best_index]

    return {
        "event": detected_event,
        "confidence": round(float(confidence), 2)
    }