import streamlit as st
import pandas as pd
import pickle

# Load trained model
with open('best_rf_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("🏡 House Price Prediction App")
st.write("Enter the house details below and get an estimated price instantly!")

# Input fields
area = st.number_input("House Area (sqft)", min_value=100, max_value=10000, value=1200)
bedrooms = st.number_input("Number of Bedrooms", min_value=1, max_value=10, value=3)
bathrooms = st.number_input("Number of Bathrooms", min_value=1, max_value=10, value=2)

airconditioning = st.selectbox("Air Conditioning", ["Yes", "No"])
furnishing = st.selectbox("Furnishing Status", ["Furnished", "Semi-Furnished", "Unfurnished"])
mainroad = st.selectbox("Near Main Road?", ["Yes", "No"])

house_age = st.number_input("House Age (Years)", min_value=0, max_value=100, value=10)

# Encode categorical inputs
airconditioning_val = 1 if airconditioning == "Yes" else 0
mainroad_val = 1 if mainroad == "Yes" else 0
furnishing_dict = {"Furnished": 2, "Semi-Furnished": 1, "Unfurnished": 0}
furnishing_val = furnishing_dict[furnishing]

# Create input DataFrame
input_data = pd.DataFrame([[
    area, bedrooms, bathrooms, airconditioning_val,
    furnishing_val, mainroad_val, house_age
]], columns=[
    'Area', 'Bedrooms', 'Bathrooms', 'Airconditioning',
    'FurnishingStatus', 'Mainroad', 'HouseAge'
])

# Predict button
if st.button("Predict Price"):
    price = model.predict(input_data)[0]
    st.success(f"🏠 Estimated House Price: **KES {price:,.0f}**")
    st.balloons()
