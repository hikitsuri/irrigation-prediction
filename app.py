import os
from flask import Flask
import joblib

app = Flask(__name__)

model = joblib.load('soil_moisture_model.pkl')

@app.route('/')
def home():
    return "Hello, this is the irrigation prediction app!"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
