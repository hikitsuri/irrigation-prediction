from flask import Flask, request, jsonify
import joblib
import os

app = Flask(__name__)

# Load your model here
model = joblib.load('soil_moisture_model.pkl')

@app.route('/')
def home():
    return "Hello, this is the irrigation prediction app! - Jim"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract features from the request
        data = request.get_json(force=True)
        features = data['features']
        prediction = model.predict([features])
        return jsonify(prediction.tolist())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
