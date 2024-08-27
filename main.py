import streamlit as st
from prediction_helper import predict


st.title("Life Style Prediction")

categorical_options = {
    'Gender': ['Female', 'Male'],
    'Region': ['Southeast', 'Northeast', 'Southwest', 'Northwest'],
    'Marital Status': ['Unmarried', 'Married'],
    'Physical Activity': ['Medium', 'Low', 'High'],
    'Stress Level': ['Medium', 'High', 'Low'],
    'Bmi Category': ['Normal', 'Overweight', 'Obesity', 'Underweight'],
    'Smoking Status': ['No Smoking', 'Occasional', 'Regular'],
    'Employment Status': ['Self-Employed', 'Freelancer', 'Salaried'],
    'Medical History': [
        'High blood pressure', 'No Disease', 'Thyroid',
        'High blood pressure & Heart disease', 'Diabetes & Thyroid',
        'Diabetes', 'Heart disease', 'Diabetes & High blood pressure',
        'Diabetes & Heart disease'
    ],
    'Insurance Plan': ['Gold', 'Silver', 'Bronze']
}

row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)
row4 = st.columns(3)
row5 = st.columns(1)



with row1[0]:
    age = st.number_input('Age', min_value = 18, step = 1, max_value = 100)
with row1[1]:
    number_of_dependants = st.number_input('Number of Dependants', min_value = 0, max_value = 5)
with row1[2]:
    income_lakhs = st.number_input("Income in Lakhs", min_value = 0, step=1, max_value = 200)

with row2[0]:
    gender = st.selectbox("Gender", categorical_options['Gender'])
with row2[1]:
    physical_activity = st.selectbox("Physical Activity", categorical_options['Physical Activity'])
with row2[2]:
    stress_level = st.selectbox("Stress Level", categorical_options['Stress Level'])

with row3[0]:
    region = st.selectbox("Region", categorical_options['Region'])
with row3[1]:
    marital_status = st.selectbox("Marital Status", categorical_options['Marital Status'])
with row3[2]:
    bmi_category = st.selectbox("BMI Category", categorical_options['Bmi Category'])

with row4[0]:
    smoking_status = st.selectbox("Smoking Status", categorical_options['Smoking Status'])
with row4[1]:
    employment_status = st.selectbox("Employment Status", categorical_options['Employment Status'])
with row4[2]:
    medical_history = st.selectbox("Medical History", categorical_options['Medical History'])


with row5[0]:
    insurance_plan = st.selectbox("Insurance Plan", categorical_options['Insurance Plan'])

input_dict = {
        'Age': age,
        'Number of Dependants': number_of_dependants,
        'Income in Lakhs': income_lakhs,
        'Gender': gender,
        'Physical Activity': physical_activity,
        'Stress Level': stress_level,
        'Region': region,
        'Marital Status': marital_status,
        'BMI Category': bmi_category,
        'Smoking Status': smoking_status,
        'Employment Status': employment_status,
        'Medical History': medical_history,
        'Insurance Plan' : insurance_plan
}

if st.button('Predict'):
    prediction = predict(input_dict)
    st.success(f"Predicted Premium: {prediction}")