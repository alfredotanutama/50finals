import sqlite3
import streamlit as st

# helper functions for home

def get_ingredients_from_db():
    conn = sqlite3.connect('ingredients.db')
    cursor = conn.cursor()

    cursor.execute("SELECT ingredient, category FROM ingredients")

    ingredients_dict = {}

    for row in cursor.fetchall():
        ingredient, category = row

        if category not in ingredients_dict:
            ingredients_dict[category] = []
        
        ingredients_dict[category].append(ingredient)
    
    conn.close()
    return ingredients_dict

# functions to make checkbox from category and append to list
def make_checkbox_from_category(category, list):
    for item in category:
        if st.checkbox(item):
            if 'oil' in item.lower():
                qty = st.number_input(f"How many milliliters of {item}?",min_value=1,step=1) 
            else:
                qty = st.number_input(f"How many grams of {item}?",min_value=1,step=1) 
            
            # add to basket
            if qty > 0:
                list.append((item, qty))