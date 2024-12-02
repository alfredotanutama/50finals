import streamlit as st  # type: ignore
from PIL import Image
from helper import *
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
expander = st.expander("More about Nasi Goreng")
expander.write('''
Nasi goreng (English pronunciation: /ˌnɑːsi ɡɒˈrɛŋ/), (Indonesian and Malay for 'fried rice') is a Southeast Asian rice dish with pieces of meat and vegetables added.
It can refer simply to fried pre-cooked rice, a meal including stir-fried rice in a small amount of cooking oil or margarine, typically spiced with kecap manis (sweet soy sauce), 
shallot, garlic, ground shrimp paste, tamarind and chilli and accompanied by other ingredients, particularly egg, chicken and prawns. 
There is also another kind of nasi goreng which is made with ikan asin (salted dried fish) which is also popular across Indonesia.
''')

with st.sidebar:
    st.title("Byte🍴Bite")
    st.markdown("*Help you Predict Bite to Bytes*")
   
st.sidebar.markdown("---")
# st.sidebar.success("Please choose the main ingredients.")

get_name = get_ingredients_from_db()

# all selected in this list
basket_selected = []

#Get the Keys of Dictionary
categories = list(get_name.keys())

# list of each category
rice = get_name['Rice']
vegetable = get_name['Vegetable']
protein = get_name['Protein']
other = get_name['Other']

#display for debugging
# dbg_dis1(categories, rice, vegetable, protein, other)
st.subheader('Rice 🍚')

selected_rice = st.radio("Choose one of the rice",key="visibility",options=rice,)
if selected_rice:
    st.info(f"**You have selected:** {selected_rice}")
    qty = st.number_input(f"How many grams of {selected_rice}?",min_value=0,step=50) 
    
    # add to basket
    basket_selected.append((selected_rice,qty))

else:
    st.info("**Please choose a rice option above.**")


# for item in rice:
#     st.checkbox(item)
st.markdown('---')
st.subheader('Vegetable 🥕🍅🫑')
make_checkbox_from_category(vegetable, basket_selected)


st.markdown('---')
st.subheader('Protein 🥚🍗🥩')
make_checkbox_from_category(protein, basket_selected)

st.markdown('---')
st.subheader('Other 🧑‍🍳')
make_checkbox_from_category(other, basket_selected)
print(basket_selected)

if basket_selected not in st.session_state:
    st.session_state["basket_selected"] = ""
if st.button("KEEP"):
    st.session_state["basket_selected"] = basket_selected
    st.write("Data Have Been Saved!")

st.markdown('---')

# total cost by selections
total_cost = 0

# Display the basket with selected items and their grams
with st.sidebar:
    st.sidebar.success("### Your Recipe 🧺🧾")
    for index, item in enumerate(basket_selected):
        if isinstance(item, tuple):
            if 'oil' in item[0].lower():
                measure_unit = 'mililiters'                
            else:
                measure_unit = 'grams'

            # Display a tuple (ingredient, units)
            st.write(f"- {item[0]} - {item[1]} {measure_unit}")
            raw_price = get_price_from_db(item[0])/1000
            rawXqty = raw_price * item[1]
            idr_price = format_rp(rawXqty)

            # Update the tuple to include measure_unit, raw_price, and rawXqty
            updated_item = item + (measure_unit, raw_price, rawXqty)  # Add new data to the tuple

            # Replace the old tuple with the updated tuple in the list
            basket_selected[index] = updated_item

            st.info(f"-- Price: {idr_price}")
            total_cost += rawXqty
            # basket_selected.append(measure_unit, rawXqty, raw_price)
        else:
            # Display non-tuple items (if any)
            st.write(f"- {item}")

#display for debugging
suggested_price = 1.5 * total_cost
dbg_dis3(basket_selected)
print(f"Total Cost = {total_cost}")
formatted_total_cost = format_rp(total_cost)
formatted_suggested = format_rp(suggested_price)

st.sidebar.markdown(f"# **Total Cost = {formatted_total_cost}**")
st.sidebar.markdown(f"# **Suggested Price = {formatted_suggested}**")
