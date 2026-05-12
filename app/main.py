import streamlit as st 
from backend.inference import run_pipeline

st.title("AI Glass Recommender")

st.markdown("Upload your photo and get personalized eyewear suggestions!")

col1, col2 = st.columns(2)

with col1:
    uploaded_file = st.file_uploader("Upload Image", type=["jpg","png"])

with col2:
    if uploaded_file:
        result = run_pipeline(uploaded_file)

        st.image(result["image"])
        st.success(f"Face Shape: {result['shape']}")
        st.write("Recommended:", result["recommendations"])

st.info(f"Because your face shape is {shape}, angular frames will suit you.")
st.image("assets/glasses/aviator.jpg")
st.download_button("Download Result", data="Your result text")