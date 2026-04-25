import streamlit as st
from graph import app

st.title("Agentic Medical AI - Chest X-ray")

uploaded_file = st.file_uploader("Upload Chest X-ray", type=["png", "jpg", "jpeg"])

if uploaded_file:
    with open("temp.jpg", "wb") as f:
        f.write(uploaded_file.read())

    state = {
        "image_path": "temp.jpg",
        "predictions": {},
        "heatmap_path": "",
        "reasoning": "",
        "report": "",
        "confidence": 0.0,
        "flags": []
    }

    result = app.invoke(state)

    st.image("temp.jpg", caption="Input X-ray")

    st.subheader("Predictions")
    st.write(result["predictions"])

    st.subheader("Confidence")
    st.write(result["confidence"])

    st.subheader("AI Reasoning")
    st.write(result["reasoning"])

    st.subheader("Medical Report")
    st.write(result["report"])

    if result["flags"]:
        st.warning(result["flags"])