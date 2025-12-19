import streamlit as st 
import pandas as pd
import joblib

model = joblib.load("KNN_heart.pkl")
scaler = joblib.load("scaler.pkl")
columns = joblib.load("columns.pkl")

st.title("💝Heart Stroke Prediction by Divy S. Shekhekhat")
st.markdown("Provide the following details to check your heart stroke risk:")


Age = st.slider("Age", 18, 120, 40)
sex = st.selectbox("sex", ['Male', 'Female'])
ChestPainType = st.selectbox("ChestPainType", ["ATA", "NAP", "TA", "ASY"])
RestingBP = st.number_input("RestingBP", 80, 120, 100)
Cholesterol = st.number_input("Cholesterol", 100, 600, 200)
FastingBS = st.selectbox("FastingBS", [1, 0])
RestingECG = st.selectbox("RestingECG", ["Normal", "ST", "LVH"])
MaxHR = st.number_input("MaxHR", 60, 220, 150)
ExerciseAngina = st.selectbox("ExerciseAngina", ['Y', 'N'])
Oldpeak = st.number_input("Oldpeak", 1.0, 6.0, 2.0)
st_slope = st.selectbox("ST_Slope", ["Up", "Flat", "Down"])

if st.button("Predict your health condition"):

        raw_input = {
        'Age': Age,
        'RestingBP': RestingBP,
        'Cholesterol': Cholesterol,
        'FastingBS': FastingBS,
        'MaxHR': MaxHR,
        'Oldpeak': Oldpeak,
        'Sex_' + sex: 1,
        'ChestPainType_' + ChestPainType: 1,
        'RestingECG_' + RestingECG: 1,
        'ExerciseAngina_' + ExerciseAngina: 1,
        'ST_Slope_' + st_slope: 1
    }
        

        input_df = pd.DataFrame([raw_input])

        for col in columns:
            if col not in input_df.columns:
                input_df[col] = 0

        input_df = input_df[columns]


        prediction = model.predict(input_df)[0]

        if prediction == 1:
            st.error("⚠️ High Risk of Heart Disease")
        else:
            st.success("✅ Low Risk of Heart Disease")