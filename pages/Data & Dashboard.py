import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.title("Data & Dashboard")
st.sidebar.write("Ini adalah konten Data")

# Check if basket_selected exists in session_state
if "basket_selected" in st.session_state:
    ingredients_list = st.session_state["basket_selected"]
    print("ingredients_list:", ingredients_list) 
    # st.write("Data kept",ingredients_list)
    print(type(ingredients_list))
    print(ingredients_list)
    # Check ingredients_list is a list, and check inside list is tuple, and check the item inside each tuple is 5
    # data's example:
    # [('Premium Rice', 100, 'grams', 15.0425, 1504.25), -> List consists of tuple, tuple consists of 5 datas
    # ('Pure Beef', 3, 'grams', 136.185, 408.555)]
    if isinstance(ingredients_list, list) and all(isinstance(item, tuple) and len(item) == 5 for item in ingredients_list):
        ingredients_df = pd.DataFrame(ingredients_list, columns=['Item','Quantity','Unit','Price/Unit','Total Price'])
        ingredients_df = ingredients_df[ingredients_df['Quantity'] > 0]

        # if not empty then show dataframe
        if not ingredients_df.empty:
            st.dataframe(ingredients_df)

            # Create a pie chart based on the 'Total Price' for each ingredient
            st.write("Price Composition Per Each Item")
            fig = px.pie(ingredients_df, values='Total Price', names='Item')
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.write("No ingredients to display because all quantities are zero.")
    else:
        st.write("Please return to Home to view this Page Again.")
else:
    ingredients_list = []
    st.write("Press KEEP Button on Homepage to show this Data")

