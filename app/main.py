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

if uploaded_file:

    image = np.array(
        Image.open(uploaded_file).convert("RGB")
    )

    result = run_pipeline(image)

    if result["image"] is not None:

    display_image = result["image"]

    # Convert BGR → RGB if needed
    if len(display_image.shape) == 3:
        display_image = display_image[:, :, ::-1]

    st.image(
        display_image,
        caption="Uploaded Image",
        use_container_width=True
    )
    
    st.subheader(f"Face Shape: {result['shape']}")

    st.subheader("Recommended Glasses")

    for item in result["recommendations"]:
        st.write(f"• {item}")