import streamlit as st 
from inference import run_pipeline
import cv2
import os

st.title("AI Glass Recommender")
st.markdown("Upload your photo and get personalized eyewear suggestions!")

uploaded_file = st.file_uploader("Upload Image", type=["jpg","png"])

result = None

if uploaded_file:
    try:
        result = run_pipeline(uploaded_file)

    except Exception as e:
        st.error(f"Pipeline error: {e}")
        result = None


if result is not None:
    if result.get("image") is not None:
        img_rgb = cv2.cvtColor(result["image"], cv2.COLOR_BGR2RGB)
        st.image(img_rgb)

    st.success(f"Face Shape: {result['shape']}")
    st.write("Recommended:", result["recommendations"])
    
else:
    st.info("Please upload an image to see results")

st.download_button(
    "Download Result",
    data="Your result text")