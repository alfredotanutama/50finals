import streamlit as st # type: ignore
from PIL import Image
image = Image.open('NasiGoreng.jpg')
st.set_page_config(
    page_title= "Byte2Bite",
    page_icon="🍴"
)

st.title("Byte🍴Bite")
st.subheader("Help you Byte the Bite")
st.image(image,caption='Best Nasi Goreng in Town', width=600)
st.sidebar.success("Select a page above.")
