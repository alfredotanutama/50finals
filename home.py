import streamlit as st  # type: ignore
from PIL import Image
from helper import get_ingredients_from_db

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

# List of items for checkboxes
# items = ['Rice', 'Proteins', 'Vegetables', 'Others']
items = get_ingredients_from_db()

# Initialize session state for checkboxes if not already done
if 'checkbox_values' not in st.session_state:
    st.session_state['checkbox_values'] = {item: False for item in items}

# Create checkboxes dynamically for each item in the list
for item in items:
    st.session_state['checkbox_values'][item] = st.checkbox(item, value=st.session_state['checkbox_values'].get(item, False))

# Display which items were selected
st.write('You selected:', [item for item, is_checked in st.session_state['checkbox_values'].items() if is_checked])



