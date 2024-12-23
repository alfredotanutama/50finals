import streamlit as st
import pandas as pd
import pickle

# Load the trained model from the file
with open('trained_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

# # Streamlit interface
# st.title('Revenue Prediction')
# Elegant Header using Markdown and HTML
st.markdown("""
    <h1 style="text-align: center; font-size: 50px; font-family: 'Arial', sans-serif; color: #4CAF50; font-weight: bold;">
        Revenue Predictor
    </h1>
    <p style="text-align: center; font-size: 20px; color: gray;">
        Predict the potential revenue based on restaurant metrics
    </p>
""", unsafe_allow_html=True)


# Collect input data from user using sliders in the sidebar
rating = st.sidebar.slider('Rating', min_value=0.0, max_value=5.0, value=4.5, step=0.1)
average_food_price = st.sidebar.slider('Average Food Price (IDR)', min_value=10000, max_value=100000, value=35000, step=500)

# dine_in = st.sidebar.selectbox('Dine In', options=[0, 1], index=1)  # 0 for No, 1 for Yes
# Use 'Yes' and 'No' for Dine In, and map to 1 for Yes and 0 for No
dine_in_option = st.sidebar.selectbox('Dine In', options=['Yes', 'No'], index=0)  # Default to 'Yes'
dine_in = 1 if dine_in_option == 'Yes' else 0

# take_away = st.sidebar.selectbox('Take Away', options=[0, 1], index=1)  # 0 for No, 1 for Yes
take_away_option = st.sidebar.selectbox('Take Away', options=['Yes', 'No'], index=0)  # Default to 'Yes'
take_away = 1 if take_away_option == 'Yes' else 0

# Create input data as a DataFrame
input_data = pd.DataFrame({
    "Rates": [rating],
    "Average Food Price (IDR)": [average_food_price],
    "Dine In": [dine_in],
    "Take Away": [take_away]
})

# Use the loaded model to make predictions
predictions = loaded_model.predict(input_data)

# Ensure the prediction is a float and format it correctly
predicted_revenue = predictions[0][0] if predictions.ndim > 1 else predictions[0]
predicted_frequency = predictions[0][1] if predictions.ndim > 1 else predictions[1]

# # Display the predicted revenue immediately
# st.write(f"Predicted Revenue: IDR {predicted_revenue:,.2f}")


# Convert the predicted revenue from IDR to USD (example conversion rate: 1 USD = 15,000 IDR)
usd_to_idr_rate = 15000
predicted_revenue_usd = predicted_revenue / usd_to_idr_rate

# Use Markdown with HTML for custom formatting
st.markdown(f"""
    <div style="text-align: center; font-size: 40px; font-weight: bold;">
        IDR {predicted_revenue:,.2f}/month
    </div>
    <div style="text-align: center; font-size: 30px; color: gray;">
        USD {predicted_revenue_usd:,.2f}/month
    </div>
    <div style="text-align: center; font-size: 20px; margin-top: 20px;">
        Predicted Frequency: {predicted_frequency:.0f} sales/month
    </div>
""", unsafe_allow_html=True)