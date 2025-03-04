import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os

# Load the trained Random Forest model
model_path = "randomforest_reg.pkl"
if os.path.exists(model_path):
    with open(model_path, "rb") as file:
        model = pickle.load(file)
else:
    st.error("Model file not found! Please check the file path.")

# Function to apply One-Hot Encoding on user input
def preprocess_input(age, sex, bmi, children, smoker, region):
    # One-hot encoding manually
    sex_male = 1 if sex == "Male" else 0
    sex_female = 1 if sex == "Female" else 0

    smoker_yes = 1 if smoker == "Yes" else 0
    smoker_no = 1 if smoker == "No" else 0

    region_northeast = 1 if region == "Northeast" else 0
    region_northwest = 1 if region == "Northwest" else 0
    region_southeast = 1 if region == "Southeast" else 0
    region_southwest = 1 if region == "Southwest" else 0

    # Convert input into a DataFrame (must match model training columns)
    input_data = pd.DataFrame([[age, bmi, children, sex_male, sex_female, smoker_yes, smoker_no,
                                region_northeast, region_northwest, region_southeast, region_southwest]],
                              columns=['age', 'bmi', 'children', 'sex_Male', 'sex_Female', 
                                       'smoker_Yes', 'smoker_No', 'region_Northeast', 
                                       'region_Northwest', 'region_Southeast', 'region_Southwest'])
    return input_data

def predict_premium(input_data):
    # Predict premium
    prediction = model.predict(input_data)
    return prediction[0]

# Streamlit UI
st.title("🏥 Insurance Premium Prediction (OHE)")
st.write("Enter your details to predict the estimated insurance premium.")

# User Inputs
age = st.number_input("Age", min_value=18, max_value=100, value=30)
sex = st.selectbox("Sex", ["Male", "Female"])
bmi = st.number_input("BMI (Body Mass Index)", min_value=10.0, max_value=50.0, value=25.0)
children = st.number_input("Number of Children", min_value=0, max_value=10, value=0)
smoker = st.selectbox("Smoker", ["Yes", "No"])
region = st.selectbox("Region", ["Northeast", "Northwest", "Southeast", "Southwest"])

if st.button("Predict Premium"):
    input_data = preprocess_input(age, sex, bmi, children, smoker, region)
    result = predict_premium(input_data)
    st.success(f"Estimated Insurance Premium: ${result:,.2f}")
