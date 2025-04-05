# Sleep Disorder Detection & Prediction

## Table of Contents
1. [Overview](#overview)  
2. [Problem Statement](#problem-statement)
4. [Setup & Installation](#setup--installation)  
5. [How to Run](#how-to-run)  
    - [Flask API](#flask-api)  
    - [Flask Web App](#flask-web-app)  
    - [Streamlit App](#streamlit-app)  
    - [Gradio App](#gradio-app)  
    - [Jupyter Notebook](#jupyter-notebook)  
6. [Usage](#usage)  
7. [File Descriptions](#file-descriptions)  
8. [License](#license)  
9. [Acknowledgments](#acknowledgments)

---

## Overview
This repository provides a **Sleep Disorder Detection & Prediction** project with multiple interfaces:
- A Flask-based API  
- A Flask-based web application  
- A Streamlit application  
- A Gradio interface  

You can use any of these interfaces to predict sleep disorders based on user input from a dataset of sleep, health, and lifestyle attributes.

---

## Problem Statement
Sleep disorders affect millions of people worldwide, often leading to reduced quality of life and serious health issues. Accurate and timely detection of sleep disorders can help individuals seek appropriate treatment and improve their well-being. This project aims to:

1. Analyze relevant health and lifestyle data (e.g., age, BMI, daily activities).  
2. Predict the likelihood of common sleep disorders.  
3. Provide a user-friendly interface for clinicians and individuals to assess their sleep health.

---


## Setup & Installation

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/your-username/Sleep-Disorder-Deployment.git
   cd Sleep-Disorder-Deployment



2. **Create Conda Env**  
   ```bash
   create conda --name disorder-prediction python==3.11
   activate disorder-prediction


3 . **Install Dependencies**  
   ```bash
   pip install -r requirements.txt


4 . ** Run Webapp and API**  
   ```bash
   python app.py



git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/devdatta95/Sleep-Disorder-Prediction-With-App.git
git push -u origin main