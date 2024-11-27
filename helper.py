import sqlite3
import streamlit

# helper functions for home

def get_ingredients_from_db():
    conn = sqlite3.connect('ingredients.db')
    cursor = conn.cursor()

    cursor.execute("SELECT ingredient FROM ingredients")

    ingredients = [row[0] for row in cursor.fetchall()]
    
    conn.close()

    return ingredients