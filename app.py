from flask import Flask, render_template, session, redirect, url_for, request, jsonify
from helper_functions import SleepForm, return_prediction, sleep_model, sleep_scaler
from config import *
import logging

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mynewsecretkey'


@app.route('/', methods=['GET', 'POST'])
def index():
    form = SleepForm()
    if form.validate_on_submit():
        try:
            session['Name'] = form.Name.data
            session['Age'] = form.Age.data
            session['Gender'] = form.Gender.data
            session['Occupation'] = form.Occupation.data
            session['Sleep Duration'] = form.sleep_duration.data
            session['Quality of Sleep'] = form.quality_of_sleep.data
            session['Physical Activity Level'] = form.physical_activity.data
            session['Stress Level'] = form.stress_level.data
            session['BMI Category'] = form.bmi_category.data
            session['Heart Rate'] = form.heart_rate.data
            session['Daily Steps'] = form.daily_steps.data
            session['systolic_bp'] = form.systolic_bp.data
            session['diastolic_bp'] = form.diastolic_bp.data
            session['feedback'] = form.feedback.data
            return redirect(url_for("prediction"))
        except Exception as e:
            logging.error("Error processing form submission: %s", e)
    return render_template('home.html', form=form)


@app.route('/prediction')
def prediction():
    try:
        data = {
            "Gender": float(session['Gender']),
            "Age": float(session['Age']),
            "Occupation": float(session['Occupation']),
            "Sleep Duration": float(session['Sleep Duration']),
            "Quality of Sleep": float(session['Quality of Sleep']),
            "Physical Activity Level": float(session['Physical Activity Level']),
            "Stress Level": float(session['Stress Level']),
            "BMI Category": float(session['BMI Category']),
            "Heart Rate": float(session['Heart Rate']),
            "Daily Steps": float(session['Daily Steps']),
            "systolic_bp": float(session['systolic_bp']),
            "diastolic_bp": float(session['diastolic_bp'])
        }
        logging.info("API/Web Prediction Request: %s", data)
        result = return_prediction(model=sleep_model, scaler=sleep_scaler, data=data)
        logging.info("API/Web Prediction Result: %s", result)
        return render_template('thankyou.html', results=result)
    except Exception as e:
        logging.error("Error during prediction: %s", e)
        return render_template('notfound.html'), 500


@app.route('/api/prediction', methods=['POST'])
def predict_api():
    try:
        data = request.json
        logging.info("API JSON Request: %s", data)
        result = return_prediction(model=sleep_model, scaler=sleep_scaler, data=data)
        logging.info("API JSON Prediction Result: %s", result)
        return jsonify({"prediction": result})
    except Exception as e:
        logging.error("Error in API prediction: %s", e)
        return jsonify({"error": str(e)}), 500


@app.errorhandler(404)
def page_not_found(e):
    return render_template('notfound.html'), 404


if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=DEBUG)

