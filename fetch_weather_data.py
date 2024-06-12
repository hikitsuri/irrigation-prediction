import requests
import csv
import time
import logging

# Setup logging
logging.basicConfig(filename='fetch_weather_data.log', level=logging.INFO, format='%(asctime)s %(message)s')

def fetch_weather():
    api_key = 'your_api_key'
    lat = '36.1699'  # Latitude for Las Vegas
    lon = '-115.1398'  # Longitude for Las Vegas
    url = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric'

    try:
        response = requests.get(url)
        response.raise_for_status()
        weather_data = response.json()

        # Extract relevant data
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        pressure = weather_data['main']['pressure']
        wind_speed = weather_data['wind']['speed']
        weather_description = weather_data['weather'][0]['description']
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())

        # Append data to CSV
        with open('weather_data.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, temperature, humidity, pressure, wind_speed, weather_description])
        
        logging.info('Data fetched and appended to CSV successfully.')

    except Exception as e:
        logging.error(f'Error fetching weather data: {e}')

if __name__ == '__main__':
    fetch_weather()
