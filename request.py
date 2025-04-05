import requests
import json

url = "http://192.168.1.57:8080/api/prediction"

payload = json.dumps({
  "Gender": 1,
  "Age": 30,
  "Occupation": 1,
  "Sleep Duration": 7.6,
  "Quality of Sleep": 7,
  "Physical Activity Level": 75,
  "Stress Level": 6,
  "BMI Category": 0,
  "Heart Rate": 70,
  "Daily Steps": 8000,
  "systolic_bp": 120,
  "diastolic_bp": 80
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
