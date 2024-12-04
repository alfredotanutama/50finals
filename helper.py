import sqlite3
import streamlit as st
import pandas as pd

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
                st.info(f"**You have selected:** {item}")
                qty = st.number_input(f"How many milliliters of {item}?",min_value=1,step=1) 
            else:
                st.info(f"**You have selected:** {item}")
                qty = st.number_input(f"How many grams of {item}?",min_value=1,step=1) 
            
            # add to basket
            if qty > 0:
                list.append((item, qty))

# get price from db
def get_price_from_db(ingredient_name):
    conn = sqlite3.connect('ingredients.db')
    cursor = conn.cursor()

    # Query price from db
    cursor.execute("SELECT price FROM Ingredients WHERE ingredient = ?", (ingredient_name,))
    price = cursor.fetchone()
    conn.close()

    if price:
        return price[0]
    else:
        print ("Price #NA")
        return None # return 0 if not found
    
# format to Rupiah    
def format_rp(number):
    # Format the number with thousands separator and two decimal places
    formatted_number = f"{number:,.2f}".replace(",", ".").replace(".", ",", 1)
    
    # Add 'Rp' in front
    formatted_number_with_currency = f"Rp {formatted_number}"
    
    return formatted_number_with_currency

def draw_something_on_top_of_page_navigation():
    st.sidebar.markdown(
        "My Logo (sidebar) should be on top of the Navigation within the sidebar"
    )


# Function to initialize or reset the database
def reset_db(cursor,conn):
    # Read the SQL script from the 'insert.sql' file
    with open('insert.sql', 'r') as file:
        sql_script = file.read()
    
    # Execute the SQL script to drop and recreate the table
    cursor.executescript(sql_script)
    conn.commit()