import streamlit as st
import pandas as pd

IMAGEPATH = "backend/images/"
DESCRIPTIONPATH = "backend/description/"

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)
with col1:
    st.image(IMAGEPATH + "photo.png", width=600)
with col2:
    st.title("Edgar Elizondo")
    with open(DESCRIPTIONPATH + "myself.txt","r") as file:
        content = file.read()
    content = content.replace("\n", " ")
    st.info (content)

content = """
Below you can find some of the apps I have builts in Python. Feel free to contact me.
"""
st.write(content)
    
col3, col4 = st.columns(2)

data = pd.read_csv("backend/data.csv", sep = ";")
with col3:
    for index, row in data[::2].iterrows():
        st.header(row["title"])
with col4:
    for index, row in data[1::2].iterrows():
        st.header(row["title"])