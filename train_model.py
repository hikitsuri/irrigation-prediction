import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib
import logging

# Setup logging
logging.basicConfig(filename='train_model.log', level=logging.INFO, format='%(asctime)s %(message)s')

def read_csv_with_error_handling(filename):
    valid_rows = []
    with open(filename, 'r') as file:
        for line in file:
            fields = line.strip().split(',')
            if len(fields) == 6:  # Original expected number of fields (including 'Weather Description')
                # Remove the last field (Weather Description)
                fields = fields[:-1]
                valid_rows.append(fields)
            elif len(fields) == 5:
                valid_rows.append(fields)
            else:
                logging.warning(f"Skipping line due to unexpected number of fields: {line.strip()}")
    
    # Create DataFrame from valid rows
    columns = ['Time', 'Temperature', 'Humidity', 'Pressure', 'Wind Speed']
    df = pd.DataFrame(valid_rows[1:], columns=valid_rows[0])  # Use first row as header
    return df

# Load the dataset with manual error handling
data = read_csv_with_error_handling('weather_data.csv')

# Ensure data types are correct
data['Temperature'] = pd.to_numeric(data['Temperature'], errors='coerce')
data['Humidity'] = pd.to_numeric(data['Humidity'], errors='coerce')
data['Pressure'] = pd.to_numeric(data['Pressure'], errors='coerce')
data['Wind Speed'] = pd.to_numeric(data['Wind Speed'], errors='coerce')

# Drop rows with NaN values
data = data.dropna()

# Simulate soil moisture data
np.random.seed(42)  # For reproducibility
data['Soil Moisture'] = np.random.normal(30, 5, len(data))

# Debug: Print the first few rows of the cleaned data
logging.info('First few rows of data:\n' + data.head().to_string())

# Preprocess data
features = data[['Temperature', 'Humidity', 'Pressure', 'Wind Speed']]
target = data['Soil Moisture']

# Split data
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Scale data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Initialize model
model = RandomForestRegressor(n_estimators=100, random_state=42)

# Train model
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
logging.info(f'Mean Squared Error: {mse}')

# Save model and scaler
joblib.dump(model, 'soil_moisture_model.pkl')
joblib.dump(scaler, 'scaler.pkl')
logging.info('Model and scaler saved successfully.')

