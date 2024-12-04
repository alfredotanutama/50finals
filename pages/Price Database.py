import sqlite3
import pandas as pd
import streamlit as st
import time
from helper import  reset_db

# Predefined category options
category_options = ["Rice", "Vegetable", "Protein", "Other"]
st.sidebar.write("Navigation")

# menus for radio button
menus = ['View', 'Add', 'Edit', 'Delete','Reset']

with st.sidebar:
    menu = st.radio('Menu', menus)

# Create connection to db
conn = sqlite3.connect('ingredients.db')
cursor = conn.cursor()

st.title("Price Database")

# Function to load data from the SQL table into a pandas DataFrame
def load_data():
    query = "SELECT * FROM Ingredients"
    df = pd.read_sql(query, conn)
    return df

# Initialize Add_flag in session_state
if 'Add_flag' not in st.session_state:
    st.session_state.Add_flag = False

if 'success_message' not in st.session_state:
    st.session_state.success_message = None

# Page view
if menu == 'View':
    df = load_data()
    # Display the DataFrame
    st.write("Current Data from SQL Table:")
    st.dataframe(df.iloc[:, 1:], use_container_width=True, hide_index=True)

elif menu == 'Add':
    st.write("Add New Ingredient in the left side bar")
    # Add a new row feature (this part is inside the sidebar)
    with st.sidebar:
        st.write("Add New Ingredient")

        # Create a form for adding new rows
        with st.form(key="add_form"):
            ingredient = st.text_input("Ingredient Name")
            indonesian_name = st.text_input("Indonesian Name")
            category = st.selectbox("Category", category_options)
            price = st.number_input("Price", min_value=0.0, step=0.01)
            
            submit_button = st.form_submit_button("Add Ingredient")

            if submit_button:
                # Validation to check if the ingredient name is empty
                if not ingredient or not indonesian_name:
                    st.error("Ingredient Name cannot be empty. Please provide a valid name.")
                else:
                    # Check if the ingredient and indonesian_name already exist in the database
                    cursor.execute("SELECT COUNT(*) FROM Ingredients WHERE ingredient = ? AND indonesian_name = ?", (ingredient, indonesian_name))
                    existing_ingredient = cursor.fetchone()[0]
        
                    if existing_ingredient > 0:
                        st.error(f"Ingredient '{ingredient}' with Indonesian name '{indonesian_name}' already exists. Please use different names.")
                    else:
                        # Insert the new row into the database
                        query = """
                        INSERT INTO Ingredients (ingredient, indonesian_name, category, price)
                        VALUES (?, ?, ?, ?)
                        """
                        cursor.execute(query, (ingredient, indonesian_name, category, price))
                        conn.commit()  # Commit the changes to the database
                        st.success(f"New ingredient '{ingredient}' added successfully!")
                        
                        # Set the Add_flag to True to display the updated data outside the sidebar
                        st.session_state.Add_flag = True

    # After adding, show updated data outside the sidebar if Add_flag is True
    if st.session_state.Add_flag:
        # Reload the data after adding the new ingredient
        df = load_data()  # Reload the data from the database
        
        # Show updated data in the main content (outside the sidebar)
        st.info("Updated Data from SQL Table:")
        st.dataframe(df.iloc[:, 1:], use_container_width=True, hide_index=True)

        # Reset Add_flag to False to prevent repeated display of data
        st.session_state.Add_flag = False

elif menu == 'Edit':
    st.write("Edit the Ingredients")
    df = load_data()
    
    # Pagination logic
    rows_per_page = 10  # Number of rows per page
    total_rows = len(df)
    num_pages = (total_rows // rows_per_page) + (1 if total_rows % rows_per_page != 0 else 0)

    # Page navigation
    page = st.selectbox("Select page", range(1, num_pages + 1))

    # Get the rows for the selected page
    start_row = (page - 1) * rows_per_page
    end_row = start_row + rows_per_page
    df_page = df.iloc[start_row:end_row]
    
    # Allow editing of the table with a unique key for each instance
    edited_df = st.data_editor(df_page, key=f"data_editor_page_{page}", use_container_width=True, disabled=['id'], hide_index=True)

    # Button to save the changes
    if st.button("Save Changes"):
        for index, row in edited_df.iterrows():
            query = f"""
            UPDATE Ingredients
            SET ingredient = ?, indonesian_name = ?, category = ?, price = ?
            WHERE id = ?
            """
            cursor.execute(query, (row['ingredient'], row['indonesian_name'], row['category'], row['price'], row['id']))
        
        conn.commit()
        # st.success("Changes saved successfully!")
        # Store the success message in session_state
        st.session_state.success_message = f"Changes saved successfully!"  # Store message
        # Reload data after saving changes
        df = load_data()
        st.rerun()
        # Display success message (if available)

    if st.session_state.success_message:
        with st.empty():
            st.success(st.session_state.success_message)
            time.sleep(1)
            st.session_state.success_message = None

elif menu == 'Delete':
    # st.write("Delete Unused Ingredient")
    # Load all ingredients from the database
    df = load_data()

    # Select an ingredient to delete from the entire list (no pagination here)
    delete_ingredient = st.selectbox("Select an ingredient to delete", df['ingredient'].tolist())

    if delete_ingredient:
        if st.button(f"Delete '{delete_ingredient}'"):
            # SQL query to delete the ingredient based on its name
            cursor.execute("DELETE FROM Ingredients WHERE ingredient = ?", (delete_ingredient,))
            conn.commit()

            # Success message after deletion
            # st.success(f"Ingredient '{delete_ingredient}' deleted successfully!")

            # Reload data to reflect the deletion
            df = load_data()

            # Store the success message in session_state
            st.session_state.success_message = f"Ingredient '{delete_ingredient}' deleted successfully!"  # Store message

            # Hide the old selectbox and show the new one
            st.rerun()


    # Display success message (if available)
    if st.session_state.success_message:
        with st.empty():
            st.success(st.session_state.success_message)
            time.sleep(1)
            st.session_state.success_message = None
elif menu == 'Reset':
    st.write("Reset to default data")
    # Confirm reset
    if st.button("Reset Database"):
        reset_db(cursor, conn)
        st.success("Database has been reset and reinitialized with default data!")


# Close connection after all operations
conn.close()
