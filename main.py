import streamlit as st

IMAGEPATH = "backend/images/"
DESCRIPTIONPATH = "backend/description/"

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)
with col1:
    st.image(IMAGEPATH + "photo.png")
with col2:
    st.title("Edgar Elizondo")
    with open(DESCRIPTIONPATH + "myself.txt","r") as file:
        content = file.read()
    content = content.replace("\n", " ")
    st.info (content)
    