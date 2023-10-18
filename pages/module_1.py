import streamlit as st

st.title("Module 1 Videos")
st.header("Upload your video")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # add a progress bar
    st.video(uploaded_file)