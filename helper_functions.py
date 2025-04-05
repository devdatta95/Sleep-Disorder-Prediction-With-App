import joblib
import numpy as np
import logging
from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, TextAreaField, SubmitField
from wtforms.validators import DataRequired
from config import *

logging.basicConfig(level=logging.INFO)

# Load the Random Forest model and scaler (saved from your notebook)
try:
    sleep_model = joblib.load(MODEL_PATH)
    sleep_scaler = joblib.load(SCALER_PATH)
    logging.info("Model and scaler loaded successfully.")
except Exception as e:
    logging.error("Error loading model or scaler: %s", e)
    sleep_model = None
    sleep_scaler = None


def return_prediction(model, scaler, data):
    """
    Expects a dictionary with keys:
      "Gender", "Age", "Occupation", "Sleep Duration", "Quality of Sleep",
      "Physical Activity Level", "Stress Level", "BMI Category",
      "Heart Rate", "Daily Steps", "systolic_bp", "diastolic_bp"

    The function converts the values to int (as in your notebook),
    scales the feature vector, and returns the predicted label.
    """
    try:
        values = list(data.values())
        arr = np.array(values, dtype=int)  # casting to int as per notebook
        arr_scaled = scaler.transform([arr])
        pred = model.predict(arr_scaled)
        labels = ["Insomnia", "None", "Sleep Apnea"]
        return labels[pred[0]]
    except Exception as e:
        logging.error("Error in return_prediction: %s", e)
        return "Error"


class SleepForm(FlaskForm):
    Name = StringField('Enter Your Full Name:', validators=[DataRequired()])
    Age = StringField('Enter Your Age:', validators=[DataRequired()])
    Gender = RadioField('Please choose your Gender:', choices=[('1', 'Male'), ('0', 'Female')],
                        validators=[DataRequired()])
    Occupation = StringField('Enter your Occupation code (numeric):', validators=[DataRequired()])
    sleep_duration = StringField('Enter your Sleep Duration (hours):', validators=[DataRequired()])
    quality_of_sleep = StringField('Enter your Quality of Sleep (1-10):', validators=[DataRequired()])
    physical_activity = StringField('Enter your Physical Activity Level (numeric):', validators=[DataRequired()])
    stress_level = StringField('Enter your Stress Level (1-10):', validators=[DataRequired()])
    bmi_category = StringField('Enter your BMI Category code (numeric):', validators=[DataRequired()])
    heart_rate = StringField('Enter your Heart Rate (bpm):', validators=[DataRequired()])
    daily_steps = StringField('Enter your Daily Steps count:', validators=[DataRequired()])
    systolic_bp = StringField('Enter your Systolic Blood Pressure:', validators=[DataRequired()])
    diastolic_bp = StringField('Enter your Diastolic Blood Pressure:', validators=[DataRequired()])
    feedback = TextAreaField('Any additional comments:')
    submit = SubmitField('Submit')
