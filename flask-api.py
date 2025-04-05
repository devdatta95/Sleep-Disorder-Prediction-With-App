from flask import Flask, request, jsonify
import logging
from config import *
import joblib
import numpy as np


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


logging.basicConfig(level=logging.INFO)
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Sleep Disorder Prediction API is running!</h1>'


@app.route('/prediction', methods=['POST'])
def predict_sleep():
    try:
        data = request.json
        logging.info("API Request: %s", data)
        result = return_prediction(model=model, scaler=scaler_model, data=data)
        logging.info("API Prediction Result: %s", result)
        return jsonify({"prediction": result})
    except Exception as e:
        logging.error("Error in prediction API: %s", e)
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run("0.0.0.0", port=5080, debug=False)
