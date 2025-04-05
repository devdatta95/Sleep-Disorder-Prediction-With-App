import gradio as gr
import numpy as np
import pickle
import joblib

# Load your pre-trained model and scaler (update the file paths as needed)
model = joblib.load("Models/RFC_MODEL.pkl")
scaler_model = joblib.load("Models/SCALER_MODEL.pkl")


def return_prediction(model, scaler, data):
    """
    Convert input data to a NumPy array, scale it, and use the model to predict.
    Returns a sleep disorder label based on the predicted index.
    """
    c = list(data.values())
    e = np.array(c, dtype=float)
    w = scaler.transform([e])
    res = model.predict(w)  # e.g., returns an index like [2]
    label = ["Insomnia", "None", "Sleep Apnea"]
    return label[res[0]]


def predict_ui(gender, age, occupation, sleep_duration, quality_of_sleep,
               physical_activity_level, stress_level, bmi_category,
               heart_rate, daily_steps, systolic_bp, diastolic_bp):
    """
    Map UI inputs to numeric codes and run the prediction pipeline.

    Categorical mappings (using ascending order):
      - Gender: Female -> 0, Male -> 1
      - Occupation: Alphabetically sorted list.
      - BMI Category: Alphabetically sorted list.
    """
    # Map Gender: "Female" becomes 0, "Male" becomes 1
    gender_code = 0 if gender == "Female" else 1

    # Define occupations in alphabetical order (as produced by a label encoder)
    occupation_options = [
        "Accountant", "Doctor", "Engineer", "Lawyer", "Manager",
        "Nurse", "Sales Representative", "Salesperson", "Scientist",
        "Software Engineer", "Teacher"
    ]
    occupation_code = occupation_options.index(occupation)

    # Define BMI categories in alphabetical order
    bmi_options = ["Normal", "Normal Weight", "Obese", "Overweight"]
    bmi_code = bmi_options.index(bmi_category)

    # Build the data dictionary with all numeric values
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

    return return_prediction(model, scaler_model, data)


# Define the Gradio interface components

# For categorical inputs, we use Radio buttons.
gender_input = gr.Radio(choices=["Female", "Male"], label="Gender (Female -> 0, Male -> 1)", value="Female")
occupation_input = gr.Radio(
    choices=[
        "Accountant", "Doctor", "Engineer", "Lawyer", "Manager",
        "Nurse", "Sales Representative", "Salesperson", "Scientist",
        "Software Engineer", "Teacher"
    ],
    label="Occupation", value="Accountant"
)
bmi_input = gr.Radio(
    choices=["Normal", "Normal Weight", "Obese", "Overweight"],
    label="BMI Category", value="Normal"
)

# For numerical inputs, we use sliders.
age_input = gr.Slider(minimum=25,
                      maximum=70,
                      step=1,
                      label="Age",
                      value=40)

sleep_duration_input = gr.Slider(minimum=5.0, maximum=10.0, step=0.1, label="Sleep Duration (hours)", value=7.0)
quality_input = gr.Slider(minimum=1, maximum=10, step=1, label="Quality of Sleep (scale 1-10)", value=7)
physical_activity_input = gr.Slider(minimum=30, maximum=100, step=1, label="Physical Activity Level (minutes)",
                                    value=60)
stress_input = gr.Slider(minimum=1, maximum=10, step=1, label="Stress Level (scale 1-10)", value=5)
heart_rate_input = gr.Slider(minimum=50, maximum=100, step=1, label="Heart Rate (BPM)", value=70)
daily_steps_input = gr.Slider(minimum=3000, maximum=15000, step=500, label="Daily Steps", value=8000)
systolic_input = gr.Slider(minimum=100, maximum=160, step=1, label="Systolic Blood Pressure", value=120)
diastolic_input = gr.Slider(minimum=60, maximum=100, step=1, label="Diastolic Blood Pressure", value=80)

# Create the Gradio interface
demo = gr.Interface(
    fn=predict_ui,
    inputs=[
        gender_input, age_input, occupation_input, sleep_duration_input,
        quality_input, physical_activity_input, stress_input, bmi_input,
        heart_rate_input, daily_steps_input, systolic_input, diastolic_input
    ],
    outputs=gr.Textbox(label="Predicted Sleep Disorder"),
    title="Sleep Disorder Prediction",
    description="Select your details below. Categorical choices are converted into numeric codes based on alphabetical order."
)

if __name__ == "__main__":
    demo.launch(share=True, debug=True)

