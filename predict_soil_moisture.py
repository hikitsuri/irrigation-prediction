import joblib
import pandas as pd

# Load model and scaler
model = joblib.load('soil_moisture_model.pkl')
scaler = joblib.load('scaler.pkl')

# Example new data (ensure this matches the training data structure and ranges)
new_data = pd.DataFrame({
    'Temperature': [30],  # Should be within 27.5 to 35.36
    'Humidity': [15],     # Should be within 9.0 to 22.0
    'Pressure': [1013],   # Should be within 1006 to 1025
    'Wind Speed': [3.5]   # Should be within 1.5 to 4.12
})

# Debug: Print new data
print("New data before scaling:", new_data)

# Scale new data
new_data_scaled = scaler.transform(new_data)

# Debug: Print scaled data
print("New data after scaling:", new_data_scaled)

# Predict
prediction = model.predict(new_data_scaled)
print(f'Predicted Soil Moisture: {prediction[0]}')
