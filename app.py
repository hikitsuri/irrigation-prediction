from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load your model here
model = joblib.load('soil_moisture_model.pkl')

@app.route('/')
def home():
    return "Hello, this is the irrigation prediction app! - Jim"

@app.route('/predict', methods=['POST'])
def predict():
    if model:
        try:
            # Extract features from the request
            data = request.get_json(force=True)
            features = data['features']
            prediction = model.predict([features])
            return jsonify(prediction.tolist())
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"error": "Model not loaded"}), 500

if __name__ == '__main__':
    app.run(debug=True)
