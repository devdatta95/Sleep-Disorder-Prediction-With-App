import streamlit as st
import numpy as np
import joblib
from config import *

# Load your pre-trained model and scaler (update the file paths as needed)
model = joblib.load(MODEL_PATH)
scaler_model = joblib.load(SCALER_PATH)

def return_prediction(model, scaler, data):
    """
    Convert input data to a NumPy array, scale it, and predict the sleep disorder.
    Returns the corresponding label.
    """
    c = list(data.values())
    e = np.array(c, dtype=float)
    w = scaler.transform([e])
    res = model.predict(w)  # e.g., returns an index like [2]
    label = ["Insomnia", "None", "Sleep Apnea"]
    return label[res[0]]

def main():
    st.title("Sleep Disorder Prediction")
    st.write("Enter your details below to predict your sleep disorder.")

    # Gender (radio button: Female -> 0, Male -> 1)
    gender = st.radio("Gender (Female -> 0, Male -> 1)", options=["Female", "Male"], index=0)
    gender_code = 0 if gender == "Female" else 1

    # Age (slider)
    age = st.slider("Age", min_value=25, max_value=70, value=40, step=1)

    # Occupation (selectbox, using alphabetical order)
    occupation_options = [
        "Accountant", "Doctor", "Engineer", "Lawyer", "Manager",
        "Nurse", "Sales Representative", "Salesperson", "Scientist",
        "Software Engineer", "Teacher"
    ]
    occupation = st.selectbox("Occupation", options=occupation_options, index=0)
    occupation_code = occupation_options.index(occupation)

    # Sleep Duration (slider, float)
    sleep_duration = st.slider("Sleep Duration (hours)", min_value=5.0, max_value=10.0, value=7.0, step=0.1)

    # Quality of Sleep (slider, integer scale 1-10)
    quality_of_sleep = st.slider("Quality of Sleep (scale 1-10)", min_value=1, max_value=10, value=7, step=1)

    # Physical Activity Level (slider, minutes)
    physical_activity_level = st.slider("Physical Activity Level (minutes)", min_value=30, max_value=100, value=60, step=1)

    # Stress Level (slider, integer scale 1-10)
    stress_level = st.slider("Stress Level (scale 1-10)", min_value=1, max_value=10, value=5, step=1)

    # BMI Category (radio button, mapped by ascending order)
    bmi_options = ["Normal", "Normal Weight", "Obese", "Overweight"]
    bmi_category = st.radio("BMI Category", options=bmi_options, index=0)
    bmi_code = bmi_options.index(bmi_category)

    # Heart Rate (slider, BPM)
    heart_rate = st.slider("Heart Rate (BPM)", min_value=50, max_value=100, value=70, step=1)

    # Daily Steps (slider)
    daily_steps = st.slider("Daily Steps", min_value=3000, max_value=15000, value=8000, step=500)

    # Systolic Blood Pressure (slider)
    systolic_bp = st.slider("Systolic Blood Pressure", min_value=100, max_value=160, value=120, step=1)

    # Diastolic Blood Pressure (slider)
    diastolic_bp = st.slider("Diastolic Blood Pressure", min_value=60, max_value=100, value=80, step=1)

    if st.button("Predict Sleep Disorder"):
        # Build data dictionary with numeric values
        data = {
            "Gender": gender_code,
            "Age": age,
            "Occupation": occupation_code,
            "Sleep Duration": sleep_duration,
            "Quality of Sleep": quality_of_sleep,
            "Physical Activity Level": physical_activity_level,
            "Stress Level": stress_level,
            "BMI Category": bmi_code,
            "Heart Rate": heart_rate,
            "Daily Steps": daily_steps,
            "systolic_bp": systolic_bp,
            "diastolic_bp": diastolic_bp
        }
        prediction = return_prediction(model, scaler_model, data)
        st.success(f"Predicted Sleep Disorder: {prediction}")

if __name__ == '__main__':
    main()
