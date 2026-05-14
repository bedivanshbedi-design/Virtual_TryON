import streamlit as st
import numpy as np
from PIL import Image

from inference import run_pipeline


st.set_page_config(page_title="AI Glass Recommender")

st.title("AI Glass Recommender")

st.write(
    "Upload your image and get glasses recommendations."
)

uploaded_file = st.file_uploader(
    "Upload Face Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    try:

        # SAFE PIL IMAGE
        pil_image = Image.open(uploaded_file).convert("RGB")

        # SAFE NUMPY IMAGE
        image = np.array(pil_image).astype(np.uint8)

        # RUN PIPELINE
        result = run_pipeline(image)

        # DISPLAY ORIGINAL IMAGE ONLY
        # (Most stable for Streamlit Cloud)
        st.image(
            pil_image,
            caption="Uploaded Image",
            use_container_width=True
        )

        # FACE SHAPE
        st.subheader(
            f"Face Shape: {result.get('shape', 'Unknown')}"
        )

        # RECOMMENDATIONS
        st.subheader("Recommended Glasses")

        recommendations = result.get(
            "recommendations",
            []
        )

        if recommendations:

            for item in recommendations:
                st.write(f"• {item}")

        else:
            st.write("No recommendations available")

    except Exception as e:

        st.error(f"Application Error: {str(e)}")