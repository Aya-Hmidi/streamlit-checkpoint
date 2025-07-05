import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# Title
st.title("🏡 House Price Estimator")

st.write("Enter the details below to estimate the house price.")

# Input features
area = st.number_input("Area (in m²):", min_value=10, max_value=1000, step=10)
bedrooms = st.slider("Number of bedrooms:", 1, 5, 3)
location = st.selectbox("Location:", ["Downtown", "Suburb", "Countryside"])

# Encode location
location_score = {"Downtown": 3, "Suburb": 2, "Countryside": 1}
loc_value = location_score[location]

# Sample fake data for training
# Each row: [area, bedrooms, location_score]
X = np.array([
    [50, 2, 3],
    [80, 3, 2],
    [120, 4, 2],
    [200, 5, 1],
    [60, 2, 3],
    [90, 3, 1],
    [150, 4, 3],
    [40, 1, 2]
])
# Prices in thousands
y = np.array([300, 250, 400, 350, 280, 230, 500, 200])

# Train model
model = LinearRegression()
model.fit(X, y)

# Prediction
if st.button("Estimate Price"):
    input_data = np.array([[area, bedrooms, loc_value]])
    price = model.predict(input_data)[0]
    st.success(f"Estimated House Price: ${round(price * 1000):,}")
