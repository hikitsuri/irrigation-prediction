from flask import Flask, request, jsonify
import joblib
import pandas as pd
from waitress import serve

app = Flask(__name__)

# Load model and scaler
model = joblib.load('soil_moisture_model.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    new_data = pd.DataFrame(data)
    
    # Scale new data
    new_data_scaled = scaler.transform(new_data)
    
    # Predict
    prediction = model.predict(new_data_scaled)
    return jsonify({'predicted_soil_moisture': prediction.tolist()})

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=5000)
