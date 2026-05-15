import cloudinary
import cloudinary.uploader

from pymongo import MongoClient
from datetime import datetime


# -------------------------
# CLOUDINARY CONFIG
# -------------------------

cloudinary.config(
    cloud_name="dqvl1rndj",
    api_key="417383256219875",
    api_secret="**********"
)

# -------------------------
# MONGODB CONFIG
# -------------------------

client = MongoClient(
    "mongodb+srv://bedivanshbedi_db_user:<db_password>@cluster0.bxvb46a.mongodb.net/?appName=Cluster0"
)

db = client["ai_glasses_db"]

collection = db["recommendations"]


# -------------------------
# SAVE FUNCTION
# -------------------------

def save_result(
    pil_image,
    result
):

    # Upload image
    upload_result = cloudinary.uploader.upload(
        pil_image
    )

    image_url = upload_result[
        "secure_url"
    ]

    # Store metadata
    data = {

        "image_url": image_url,

        "face_shape": result[
            "shape"
        ],

        "event": result[
            "event"
        ],

        "recommendations": result[
            "recommendations"
        ],

        "timestamp": datetime.utcnow()
    }

    collection.insert_one(data)

    return image_url