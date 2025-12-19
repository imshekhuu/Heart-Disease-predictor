import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/predict"

st.title("💝 Heart Stroke Prediction by Divya S. Shekhawat")
st.markdown("Provide the following details to check your heart stroke risk:")

Age = st.slider("Age", 18, 120, 40)
sex = st.selectbox("Sex", ["Male", "Female"])
ChestPainType = st.selectbox("Chest Pain Type", ["ATA", "NAP", "TA", "ASY"])
RestingBP = st.number_input("RestingBP", 80, 200, 100)
Cholesterol = st.number_input("Cholesterol", 100, 600, 200)
FastingBS = st.selectbox("FastingBS", [0, 1])
RestingECG = st.selectbox("RestingECG", ["Normal", "ST", "LVH"])
MaxHR = st.number_input("MaxHR", 60, 220, 150)
ExerciseAngina = st.selectbox("Exercise Angina", ["Y", "N"])
Oldpeak = st.number_input("Oldpeak", 0.0, 6.0, 2.0)
st_slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])


payload = {
    "Age": Age,
    "sex": sex,
    "ChestPainType": ChestPainType,
    "RestingBP": RestingBP,
    "Cholesterol": Cholesterol,
    "FastingBS": FastingBS,
    "RestingECG": RestingECG,
    "MaxHR": MaxHR,
    "ExerciseAngina": ExerciseAngina,
    "Oldpeak": Oldpeak,
    "st_slope": st_slope
}

if st.button("Predict"):
    try:
        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:
            result = response.json()
            prediction = result["prediction"]

            if prediction == 1:
                st.error("⚠️ High Risk of Heart Disease")
            else:
                st.success("✅ Low Risk of Heart Disease")
            # st.success(f"Your health condition: {result['prediction']}")

        else:
            st.error(f"API error {response.status_code}: {response.text}")

    except requests.exceptions.ConnectionError:
        st.error("Could not connect to API server. Make sure FastAPI is running on port 8000.")
