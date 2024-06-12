# Irrigation Prediction

## Overview
This project predicts soil moisture based on weather data using a machine learning model.

## Setup Instructions

### Prerequisites
- Python 3.x
- Required Python packages (install using `pip install -r requirements.txt`)

### Data Fetching
1. **`fetch_weather_data.py`**: Fetches weather data and appends it to `weather_data.csv`.
2. **`run_weather_script.bat`**: Batch file to run the data fetching script.

### Model Training
1. **`train_model.py`**: Preprocesses data and trains the machine learning model.

### Prediction
1. **`predict_soil_moisture.py`**: Uses the trained model to make predictions based on new weather data.

## Usage

1. **Set up Task Scheduler** to run `run_weather_script.bat` at desired intervals.
2. **Run `train_model.py`** to train the model periodically.
3. **Run `predict_soil_moisture.py`** to make predictions.

## Example Output
Include example outputs and usage tips.

## License
[Specify your license here]
