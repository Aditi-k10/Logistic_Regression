import streamlit as st
import pickle
import numpy as np

# Load the trained model and scaler
classifier = pickle.load(open("logistic_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

st.title("Logistic Regression Prediction App")

# User input for features (replace with your actual feature names)
feature1 = st.number_input("Enter value for Feature 1")
feature2 = st.number_input("Enter value for Feature 2")
feature3 = st.number_input("Enter value for Feature 3")
feature4 = st.number_input("Enter value for Feature 4")
feature5 = st.number_input("Enter value for Feature 5")
feature6 = st.number_input("Enter value for Feature 6")
feature7 = st.number_input("Enter value for Feature 7")
feature8 = st.number_input("Enter value for Feature 8")

# Combine inputs into a numpy array and scale
input_data = np.array([[feature1, feature2, feature3, feature4,
                        feature5, feature6, feature7, feature8]])
input_data_scaled = scaler.transform(input_data)

# Predict button
if st.button("Predict"):
    prediction = classifier.predict(input_data_scaled)
    st.success(f"The predicted class is: {prediction[0]}")
