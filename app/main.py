import streamlit as st
import numpy as np
from PIL import Image
from database import save_result

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

user_text = st.text_input(
    "Where are you planning to wear these glasses?",
    placeholder="Example: Wedding, office meeting, party, college..."
)

if uploaded_file is not None:

    try:

        # SAFE PIL IMAGE
        pil_image = Image.open(uploaded_file).convert("RGB")

        # SAFE NUMPY IMAGE
        image = np.array(pil_image).astype(np.uint8)

        # RUN PIPELINE
        result = run_pipeline(image, user_text)

        # DISPLAY ORIGINAL IMAGE ONLY
        # (Most stable for Streamlit Cloud)

        st.image(
            pil_image,
            caption="Uploaded Image",
            use_column_width=True
        )

        # FACE SHAPE
        st.subheader(
            f"Detected Face Shape: {result['shape']}"
        )

        # DETECTED EVENT
        st.subheader(
            f"Detected Event: {result['event']}"
        )

        st.write(
            f"NLP Confidence: {result['event_confidence']}"
        )

        # RECOMMENDATIONS
        st.subheader(
            "Recommended Glasses"
        )

        for item in result[
            "recommendations"
        ]:

            st.write(f"• {item}")

        # DEBUG METRICS
        with st.expander(
            "Face Metrics"
        ):

            st.write(
                result["metrics"]
            )

    except Exception as e:

        st.error(
            f"Application Error: {str(e)}"
        )

image_url = save_result(
    pil_image,
    result
)

st.success(
    "Image saved successfully!"
)

st.write(image_url)