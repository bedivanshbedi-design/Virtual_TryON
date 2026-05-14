import streamlit as st
from inference import run_pipeline

from PIL import Image
import numpy as np

st.title("AI Glass Recommender")
st.markdown("Upload your photo and get personalized eyewear suggestions!")

uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png"])

result = None

if uploaded_file:
    try:
        # ✅ Convert uploaded file → numpy image (InsightFace compatible)
        image = np.array(Image.open(uploaded_file).convert("RGB"))

        # ✅ Pass numpy image (NOT raw file)
        result = run_pipeline(image)

    except Exception as e:
        st.error(f"Pipeline error: {e}")
        result = None


# ✅ Show results
if result is not None:

    # ✅ Display processed image safely (NO cv2)
    if isinstance(result, dict) and result.get("image") is not None:
        st.image(result["image"])

    if isinstance(result, dict):
        st.success(f"Face Shape: {result.get('shape', 'Unknown')}")
        st.write("Recommended:", result.get("recommendations", []))

    else:
        # fallback if run_pipeline returns string
        st.success(f"Face Shape: {result}")

else:
    st.info("Please upload an image to see results")


# ✅ Download button (simple text export)
st.download_button(
    "Download Result",
    data=str(result),
    file_name="result.txt"
)
