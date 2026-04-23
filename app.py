import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("🔥 Calories Burn Prediction App")
st.write("Enter your details below 👇")

# Inputs
age = st.number_input("Age", min_value=1, max_value=100, value=25)
gender = st.selectbox("Gender (0 = Female, 1 = Male)", [0, 1])
height = st.number_input("Height (cm)")
weight = st.number_input("Weight (kg)")
duration = st.number_input("Duration (minutes)", min_value=1, max_value=300, value=30)
heart_rate = st.number_input("Heart Rate", min_value=60, max_value=200, value=100)
body_temp = st.number_input("Body Temperature (°C)", min_value=35.0, max_value=42.0, value=37.0)

# SAME order as training
input_data = np.array([[gender, age, height, weight, duration, heart_rate, body_temp]])

# Predict
if st.button("🔥 Predict Calories"):
    prediction = model.predict(input_data)
    st.success(f"🔥 Estimated Calories Burned: {float(prediction[0]):.2f}")