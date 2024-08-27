import pandas as pd
from joblib import load

model = load("artifacts\model.joblib")
scaler1 = load("artifacts\scaler.joblib")

def calculate_normalized_risk_score(medical_history):
    risk_scores = {
            'diabetes': 6,
            'heart disease': 8,
            'high blood pressure': 6,
            'thyroid': 5,
            'no disease': 0,
            'none': 0
        }
    diseases = medical_history.lower().split(" & ")

    total_risk_score =sum(risk_scores.get(disease,0) for disease in diseases)

    max_score =14
    min_score =0

    normalized_risk_score = (total_risk_score - min_score) / (max_score - min_score)

    return normalized_risk_score

def calculate_life_style_risk_score(physical_activity, stress_level):
    physical_activity_risk_score = {
        "High": 0,
        "Medium": 1,
        "Low": 4
    }
    
    stress_risk_score = {
        "High": 4,
        "Medium": 1,
        "Low": 0
    }
    
    # Map the risk scores
    physical_activity_score = physical_activity_risk_score.get(physical_activity, 0)
    stress_score = stress_risk_score.get(stress_level, 0)
    
    # Sum the scores to get the lifestyle risk score
    life_style_risk_score = physical_activity_score + stress_score
    
    return life_style_risk_score
    







def preprocess_input(input_dict):
    expected_columns = [
             'age',	'number_of_dependants',	'income_lakhs',	'insurance_plan', 'normalized_risk_score', 'life_style_risk_score',	
             'gender_Male',	'region_Northwest',	'region_Southeast',	'region_Southwest',	'marital_status_Unmarried',	
             'bmi_category_Obesity', 'bmi_category_Overweight',	'bmi_category_Underweight',	
             'smoking_status_Occasional', 'smoking_status_Regular',	'employment_status_Salaried', 'employment_status_Self-Employed'
]
    insurance_plan_encoding = {'Bronze': 1, 'Silver': 2, 'Gold': 3}
    physical_activity = input_dict['Physical Activity']
    stress_level = input_dict['Stress Level']
    df = pd.DataFrame(0, columns=expected_columns, index=[0])

    for key ,value in input_dict.items():
        
        if key == 'Gender' and value == 'Male':
            df['gender_Male'] = 1
        if key == 'Region' and value == 'Northwest':
            df['region_Northwest'] = 1
        if key == 'Region' and value == 'Southeast':
            df['region_Southeast'] = 1
        if key == 'Region' and value == 'Southwest':
            df['region_Southwest'] = 1
        if key == 'Marital Status' and value == 'Unmarried':
            df['marital_status_Unmarried'] = 1
        if key == 'BMI Category' and value == 'Obesity':
            df['bmi_category_Obesity'] = 1
        if key == 'BMI Category' and value == 'Overweight':
            df['bmi_category_Overweight'] = 1
        if key == 'BMI Category' and value == 'Underweight':
            df['bmi_category_Underweight'] = 1
        if key == 'Smoking Status' and value == 'Occasional':
            df['smoking_status_Occasional'] = 1
        if key == 'Smoking Status' and value == 'Regular':
            df['smoking_status_Regular'] = 1
        if key == 'Employment Status' and value == 'Salaried':
            df['employment_status_Salaried'] = 1
        if key == 'Employment Status' and value == 'Self-Employed':
            df['employment_status_Self-Employed'] = 1
        if key == 'Insurance Plan':
            df['insurance_plan'] = insurance_plan_encoding.get(value,1)
        if key == 'Age':
            df['age'] = value
        if key == 'Number of Dependants':
            df['number_of_dependants'] = value
        if key == 'Income in Lakhs':
            df['income_lakhs'] = value
    
    df['normalized_risk_score'] = calculate_normalized_risk_score(input_dict['Medical History'])
  
    df['life_style_risk_score'] = calculate_life_style_risk_score(physical_activity ,stress_level)
    df = handle_scaling(df)
    return df


def handle_scaling(df):
    scaler_object = scaler1
    cols_to_scale = scaler_object['cols_to_scale']
    scaler = scaler_object['scaler']

    df['income_level'] = None
    df[cols_to_scale] = scaler.transform(df[cols_to_scale])
    df.drop('income_level', axis = 'columns', inplace = True)
    return df






def predict(input_dict):
    input_df = preprocess_input(input_dict)
    prediction = model.predict(input_df)

    return int(prediction)