import requests
import csv
import datetime

API_KEY = 'b81e63b74800d3331f67fa47e1c35e29'  
LOCATION = 'Las Vegas'
URL = f'http://api.openweathermap.org/data/2.5/weather?q={LOCATION}&appid={API_KEY}&units=imperial'

response = requests.get(URL)
weather_data = response.json()

# Print to verify units
print(weather_data)

# Extract necessary fields
temperature = weather_data['main']['temp']
humidity = weather_data['main']['humidity']
timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Append data to CSV
with open('weather_data.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([timestamp, temperature, humidity])
