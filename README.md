# Irrigation Prediction App

## Description
This project is an irrigation prediction app that uses a machine learning model to predict soil moisture levels based on input features. The application is deployed on Heroku.

## Features
- Predict soil moisture levels using a trained model
- Easy-to-use API for predictions

## Installation

### Prerequisites
- Python 3.9
- pip

### Clone the Repository
```bash
git clone https://github.com/yourusername/irrigation-prediction.git
cd irrigation-prediction

Install Dependencies

bash
pip install -r requirements.txt
Usage

Run the Application

bash
python app.py
Predict Soil Moisture
Send a POST request to the /predict endpoint with input features:

bash
curl -X POST -H "Content-Type: application/json" -d "{\"features\": [1, 2, 3, 4]}" https://irrigation-prediction-d56529386fb6.herokuapp.com/predict
Deployment
Deploy on Heroku
Create a new Heroku app:

bash
heroku create
Push your code to Heroku:

bash
git push heroku main

Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.


