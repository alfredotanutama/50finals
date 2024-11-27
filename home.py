import streamlit as st  # type: ignore
from PIL import Image
from helper import get_ingredients_from_db
from debugdisplay import *

# Set up the page configuration
st.set_page_config(
    page_title="Byte2Bite",
    page_icon="🍴"
)

# Title and subtitle
st.title("Byte🍴Bite")
st.markdown("*Help you Predict Bite to Bytes*")

# Load and display the main image
image = Image.open('NasiGoreng.jpg')
st.image(image, caption='Best Nasi Goreng in Town', use_container_width=True)
st.sidebar.markdown("---")
st.sidebar.success("Please choose the main ingredients.")

get_name = get_ingredients_from_db()

#Get the Keys of Dictionary
categories = list(get_name.keys())

# list of each category
rice = get_name['Rice']
vegetable = get_name['Vegetable']
protein = get_name['Protein']
other = get_name['Other']

dbg_dis1(categories, rice, vegetable, protein, other)


