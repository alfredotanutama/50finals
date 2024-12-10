import streamlit as st
import pandas as pd
import pickle

# Load the trained model (make sure it's been pickled beforehand)
with open('revenue_predictor_random_tuning_2.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

# Feature names used during training (ensure this matches the model's input features)
feature_names = [
    "Rating", "Seating Capacity", "Average Meal Price", "Marketing Budget",
    "Social Media Followers", "Chef Experience Years", "Number of Reviews",
    "Avg Review Length", "Ambience Score", "Service Quality Score",
    "Weekend Reservations", "Weekday Reservations", "Location_Rural",
    "Location_Suburban", "Cuisine_French", "Cuisine_Indian",
    "Cuisine_Italian", "Cuisine_Japanese", "Cuisine_Mexican",
    "Parking Availability_Yes"
]

# Streamlit interface
st.title('Restaurant Revenue Prediction')

# Collect input data from user using sliders in the sidebar
rating = st.sidebar.slider('Rating', min_value=0.0, max_value=5.0, value=4.5, step=0.1)
seating_capacity = st.sidebar.slider('Seating Capacity', min_value=10, max_value=500, value=120)
average_meal_price = st.sidebar.slider('Average Meal Price', min_value=10.0, max_value=100.0, value=25.0, step=0.5)
marketing_budget = st.sidebar.slider('Marketing Budget', min_value=1000, max_value=20000, value=5000, step=500)
social_media_followers = st.sidebar.slider('Social Media Followers', min_value=0, max_value=1000000, value=200)
chef_experience_years = st.sidebar.slider('Chef Experience (Years)', min_value=1, max_value=50, value=10)
number_of_reviews = st.sidebar.slider('Number of Reviews', min_value=0, max_value=10000, value=300)
avg_review_length = st.sidebar.slider('Average Review Length', min_value=0.0, max_value=10.0, value=4.5, step=0.1)
ambience_score = st.sidebar.slider('Ambience Score', min_value=0.0, max_value=10.0, value=8.0, step=0.1)
service_quality_score = st.sidebar.slider('Service Quality Score', min_value=0.0, max_value=10.0, value=7.5, step=0.1)
weekend_reservations = st.sidebar.slider('Weekend Reservations', min_value=0, max_value=1000, value=90)
weekday_reservations = st.sidebar.slider('Weekday Reservations', min_value=0, max_value=1000, value=70)

# Location selection using radio buttons (Rural vs Suburban)
location_rural = st.sidebar.radio('Location: Rural', options=[0, 1], index=0, format_func=lambda x: 'Yes' if x == 1 else 'No')
location_suburban = st.sidebar.radio('Location: Suburban', options=[0, 1], index=1, format_func=lambda x: 'Yes' if x == 1 else 'No')

# Cuisine selection using radio buttons with choices
cuisine_options = ['French', 'Indian', 'Italian', 'Japanese', 'Mexican']
cuisine_choice = st.sidebar.radio('Cuisine Type', options=cuisine_options)

# Convert cuisine choice to one-hot encoding (assuming one-hot encoding is used)
cuisine_french = 1 if cuisine_choice == 'French' else 0
cuisine_indian = 1 if cuisine_choice == 'Indian' else 0
cuisine_italian = 1 if cuisine_choice == 'Italian' else 0
cuisine_japanese = 1 if cuisine_choice == 'Japanese' else 0
cuisine_mexican = 1 if cuisine_choice == 'Mexican' else 0

# Parking availability as a radio button
parking_availability = st.sidebar.radio('Parking Availability (Yes)', options=[0, 1], index=1, format_func=lambda x: 'Yes' if x == 1 else 'No')

# Create input data based on slider values
input_data = [
    rating, seating_capacity, average_meal_price, marketing_budget,
    social_media_followers, chef_experience_years, number_of_reviews,
    avg_review_length, ambience_score, service_quality_score,
    weekend_reservations, weekday_reservations, location_rural, location_suburban,
    cuisine_french, cuisine_indian, cuisine_italian, cuisine_japanese,
    cuisine_mexican, parking_availability
]

# Convert the input data into a DataFrame with the feature names
input_df = pd.DataFrame([input_data], columns=feature_names)

# Add a button for prediction
if st.button('Predict Revenue'):
    print(input_data)
    
    predicted_revenue = loaded_model.predict(input_df)
    st.write(f"Predicted Revenue: ${predicted_revenue[0]:,.2f}")
else:
    st.write("Click the button to predict revenue.")
