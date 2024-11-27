import streamlit as st  # type: ignore
from PIL import Image

# Set up the page configuration
st.set_page_config(
    page_title="Byte2Bite",
    page_icon="🍴"
)

# Title and subtitle
st.title("Byte🍴Bite")
st.markdown("*Help you Bite to Bytes*")

# Load and display the main image
image = Image.open('NasiGoreng.jpg')
st.image(image, caption='Best Nasi Goreng in Town', use_container_width=True)
st.sidebar.success("Select a page above.")

# List of items for checkboxes
items = ['Rice', 'Proteins', 'Vegetables', 'Others']

# Display an info message
st.info('Please choose the main ingredients you used.')

# Create two columns for layout
col1, col2 = st.columns([1, 2]) 

# Initialize selected_items list
selected_items = ['Rice']  # Start with Rice always selected

# Display Rice checkbox and image
with col1:
    st.checkbox('Rice', value=True, disabled=True)  # Display Rice as checked but disabled
    rice_image = Image.open('nasi.jpeg')  
    st.image(rice_image, caption='Cooked Rice', use_container_width=True)

with col2:
    rice_quantity = st.slider('Select quantity of Rice', 1, 10, 1)
    st.info(f'You selected {rice_quantity} servings of Rice.')

st.markdown("---")

# Creating checkboxes dynamically for other items
for item in items[1:]:
    # Create new columns for each item
    col1, col2 = st.columns([1, 2])  # Adjust the ratios here

    with col1:
        checkbox_value = st.checkbox(item)  # Store the checkbox state
        if checkbox_value:
            selected_items.append(item)
            # Display images based on selected items
            if item == 'Proteins':
                protein_image = Image.open('protein.jpg')  
                st.image(protein_image, caption='Protein', use_container_width=True)
            elif item == 'Vegetables':
                vegetable_image = Image.open('sayur.jpg')  
                st.image(vegetable_image, caption='Vegetables', use_container_width=True)
            elif item == 'Others':
                others_image = Image.open('others.jpg')  # Replace with your image path
                st.image(others_image, caption='Other Ingredients', use_container_width=True)

    with col2:
        # Show sliders only if the corresponding checkbox is checked
        if item == 'Proteins' and checkbox_value:
            egg_quantity = st.slider('Select quantity of Eggs', 0, 10)
            st.info(f'You selected {egg_quantity} servings of Egg.')
            chicken_quantity = st.slider('Select quantity of Chicken', 0, 10)
            st.info(f'You selected {chicken_quantity} servings of Chicken.')
        elif item == 'Vegetables' and checkbox_value:
            vegetable_quantity = st.slider('Select quantity of Vegetables', 1, 10, 1)
            st.info(f'You selected {vegetable_quantity} servings of Vegetables.')
        elif item == 'Others' and checkbox_value:
            others_quantity = st.slider('Select quantity of Other Ingredients', 1, 10, 1)
            st.info(f'You selected {others_quantity} servings of Other Ingredients.')

    # Add a divider after processing both columns
    st.markdown("---")

# Displaying selected items (optional)
st.write('You selected:', selected_items)