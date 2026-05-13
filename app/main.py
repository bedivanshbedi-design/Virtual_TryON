import streamlit as st 
from inference import run_pipeline
import cv2
import os

st.title("AI Glass Recommender")
st.markdown("Upload your photo and get personalized eyewear suggestions!")

col1, col2 = st.columns(2)

with col1:
    uploaded_file = st.file_uploader("Upload Image", type=["jpg","png"])

with col2:
    if uploaded_file is not None:
        result = run_pipeline(uploaded_file)

    if result["image"] is not None:
        img_rgb = cv2.cvtColor(result["image"], cv2.COLOR_BGR2RGB)
        st.image(img_rgb)

        st.success(f"Face Shape: {result['shape']}")
        st.write("Recommended:", result["recommendations"])
    
    else:
        st.info("Please upload an image to see results")

st.download_button(
    "Download Result",
    data="Your result text")