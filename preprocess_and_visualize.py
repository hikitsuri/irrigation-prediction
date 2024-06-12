import pandas as pd
import matplotlib.pyplot as plt

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
                print(f"Skipping line due to unexpected number of fields: {line.strip()}")
    
    # Create DataFrame from valid rows
    columns = ['Time', 'Temperature', 'Humidity', 'Pressure', 'Wind Speed', 'Soil Moisture']
    df = pd.DataFrame(valid_rows[1:], columns=valid_rows[0])  # Use first row as header
    return df

# Load the dataset with manual error handling
df = read_csv_with_error_handling('weather_data.csv')

# Ensure data types are correct
df['Temperature'] = pd.to_numeric(df['Temperature'], errors='coerce')
df['Humidity'] = pd.to_numeric(df['Humidity'], errors='coerce')
df['Pressure'] = pd.to_numeric(df['Pressure'], errors='coerce')
df['Wind Speed'] = pd.to_numeric(df['Wind Speed'], errors='coerce')

# Check if 'Soil Moisture' column exists and convert to numeric
if 'Soil Moisture' in df.columns:
    df['Soil Moisture'] = pd.to_numeric(df['Soil Moisture'], errors='coerce')
else:
    print("'Soil Moisture' column is missing in the CSV file.")

# Drop rows with NaN values
df = df.dropna()

# Plot the data
plt.figure(figsize=(10, 6))

# Plot temperature over time
plt.subplot(2, 2, 1)
plt.plot(df['Temperature'], marker='o', linestyle='-', color='b')
plt.title('Temperature Over Time')
plt.xlabel('Time')
plt.ylabel('Temperature (°C)')

# Plot humidity over time
plt.subplot(2, 2, 2)
plt.plot(df['Humidity'], marker='o', linestyle='-', color='g')
plt.title('Humidity Over Time')
plt.xlabel('Time')
plt.ylabel('Humidity (%)')

# Plot pressure over time
plt.subplot(2, 2, 3)
plt.plot(df['Pressure'], marker='o', linestyle='-', color='r')
plt.title('Pressure Over Time')
plt.xlabel('Time')
plt.ylabel('Pressure (hPa)')

# Plot wind speed over time
plt.subplot(2, 2, 4)
plt.plot(df['Wind Speed'], marker='o', linestyle='-', color='c')
plt.title('Wind Speed Over Time')
plt.xlabel('Time')
plt.ylabel('Wind Speed (m/s)')

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()

