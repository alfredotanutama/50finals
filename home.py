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

# List of items for checkboxes
items = [
    'Rice',
    'Chicken',
    'Eggs',
    'Shallots',
    'Garlic',
    'Spring Onions',
    'Sweet Soy Sauce',
    'Oyster Sauce',
    'Light Soy Sauce',
    'Sugar',
    'Pepper',
    'Margarine',
    'Mushroom Broth',
    'Oil'
]

st.info('Please choose the main ingredients you used.')

# Creating checkboxes dynamically
selected_items = ['Rice']  # Start with Rice always selected
st.checkbox('Rice', value=True, disabled=True)  # Display Rice as checked but disabled

# Creating checkboxes dynamically
for item in items[1:]:
    # 'Rice' is always checked
    if item == 'Rice':
        if st.checkbox(item, value=True):  # Rice is always checked
            selected_items.append(item)

    if st.checkbox(item):
        selected_items.append(item)



# Displaying selected items
st.write('You selected:', selected_items)

#gambar nasi terus nanti bisa berubah tergantung bumbu