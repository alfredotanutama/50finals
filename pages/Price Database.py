import sqlite3
import pandas as pd
import streamlit as st
# Predefined category options
category_options = ["Rice", "Vegetable", "Protein", "Other"]
st.sidebar.write("Ini adalah konten Data ")

# Create connection to db
conn = sqlite3.connect('ingredients.db')

# Create cursor object
cursor = conn.cursor()

st.title("Price Database")


# Function to load data from the SQL table into a pandas DataFrame
def load_data():
    query = "SELECT * FROM Ingredients"
    df = pd.read_sql(query, conn)
    return df

df = load_data()

# # Display the DataFrame
# st.write("Current Data from SQL Table:")
# st.dataframe(df)

with st.sidebar:
    # Add a new row feature
    st.subheader("Add New Ingredient")

    # Create a form for adding new rows
    with st.form(key="add_form"):
        ingredient = st.text_input("Ingredient Name")
        indonesian_name = st.text_input("Indonesian Name")
        category =  st.selectbox("Category", category_options)
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
                # If both ingredient and indonesian_name exist, show an error message
                    st.error(f"Ingredient '{ingredient}' with Indonesian name '{indonesian_name}' already exists. Please use different names.")
                else:
                    # Insert the new row into the database
                    query = """
                    INSERT INTO Ingredients (ingredient, indonesian_name, category, price)
                    VALUES (?, ?, ?, ?)
                    """
                    cursor.execute(query, (ingredient, indonesian_name, category, price))
                    conn.commit()
                    st.success(f"New ingredient '{ingredient}' added successfully!")

                    # After submission, clear the input fields
                    st.session_state['ingredient_input'] = ''
                    st.session_state['indonesian_name_input'] = ''
                    st.session_state['category_input'] = ''
                    st.session_state['price_input'] = ''   

                    # Reload data to reflect the new row
                    df = load_data()
                    # st.dataframe(df,use_container_width=True)

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

# Hide the 'id' column before displaying the dataframe
# df_page_without_id = df_page.drop(columns=['id'])
# df_page_without_id.index = df_page_without_id.index + 1


# Allow editing of the table with a unique key for each instance
edited_df = st.data_editor(df_page, key=f"data_editor_page_{page}")


# Button to save the changes
if st.button("Save Changes/ Refresh"):
    for index, row in edited_df.iterrows():
        # Assuming the primary key column is 'id' and is used for updates
        query = f"""
        UPDATE Ingredients
        SET ingredient = ?, indonesian_name = ?, category = ?, price = ?
        WHERE id = ?
        """
        cursor.execute(query, (row['ingredient'], row['indonesian_name'], row['category'], row['price'],row['id']))
    
    conn.commit()
    st.success("Changes saved/ refreshed successfully!")

# Add delete dropdown functionality below the table
delete_ingredient = st.selectbox("Select an ingredient to delete", df_page['ingredient'].tolist(), key="delete_ingredient_select")

if delete_ingredient:
    if st.button(f"Delete '{delete_ingredient}'"):
        # SQL query to delete the ingredient based on its name
        cursor.execute("DELETE FROM Ingredients WHERE ingredient = ?", (delete_ingredient,))
        conn.commit()

        # Success message after deletion
        st.success(f"Ingredient '{delete_ingredient}' deleted successfully!")

        # Reload data to reflect the deletion
        df = load_data()  # Reload the full data to get the latest data

# Close the connection
conn.close()