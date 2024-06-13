import os
from flask import Flask, jsonify
import joblib

app = Flask(__name__)

try:
    model = joblib.load('soil_moisture_model.pkl')
except Exception as e:
    model = None
    print(f"Error loading model: {e}")

@app.route('/')
def home():
    return "Hello, this is the irrigation prediction app! - Jim"

@app.route('/predict', methods=['GET'])
def predict():
    if model:
        # Example input features for prediction
        example_input = [[1, 2, 3, 4]]  # Replace with actual input format
        try:
            prediction = model.predict(example_input)
            return jsonify(prediction.tolist())
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"error": "Model not loaded"}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
