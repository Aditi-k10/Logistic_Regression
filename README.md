# Diabetes Disease Prediction using Logistic Regression

## Project Overview
This project predicts whether a person is diabetic or not using a machine learning model.
The model is trained using a diabetes medical dataset and deployed as a web application using Streamlit.

## Dataset Description
The dataset contains the following medical attributes:
- Pregnancies
- Glucose
- BloodPressure
- SkinThickness
- Insulin
- BMI
- DiabetesPedigreeFunction
- Age

Target Variable:
- 0 → Non-Diabetic
- 1 → Diabetic

## Machine Learning Algorithm
- Logistic Regression (Binary Classification)

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit

## Features of the Application
- Simple and user-friendly interface
- Accepts medical input parameters
- Uses StandardScaler for feature scaling
- Predicts diabetes status accurately

## Project Structure
- app.py – Streamlit application code  
- logistic_model.pkl – Trained Logistic Regression model  
- scaler.pkl – Feature scaler used for preprocessing  
- requirements.txt – Required Python libraries  

## How to Run the Project Locally
1. Clone the repository  
   git clone https://github.com/Aditi-k10/Logistic_Regression.git

2. Install dependencies  
   pip install -r requirements.txt

3. Run the Streamlit application  
   streamlit run app.py

## Deployment
The application is deployed using Streamlit Cloud.
Live Application:
https://logisticregression-js6dbvoatj7n6aj6u9pkk3.streamlit.app/
