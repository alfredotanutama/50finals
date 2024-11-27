import sqlite3
import streamlit

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