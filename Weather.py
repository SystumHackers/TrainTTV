import requests
import tkinter as tk

# Replace 'YOUR_API_KEY' with your actual weatherapi.com API key
API_KEY = '0b723cdac503424aac1173052231310'
BASE_URL = 'https://api.weatherapi.com/v1/current.json'

def get_weather(city_name):
    params = {
        'key': API_KEY,
        'q': city_name,
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        temperature = weather_data['current']['temp_c']
        condition = weather_data['current']['condition']['text']
        return f"Weather in {city_name}:\nTemperature: {temperature}°C\nCondition: {condition}"
    else:
        return f"Failed to retrieve weather data for {city_name}"

def display_weather():
    city_name = city_entry.get()
    weather_info = get_weather(city_name)
    result_label.config(text=weather_info)

# Create a Tkinter window
root = tk.Tk()
root.title("Weather Information")

# Create and configure widgets
city_label = tk.Label(root, text="Enter city name:")
city_entry = tk.Entry(root)
get_weather_button = tk.Button(root, text="Get Weather", command=display_weather)
result_label = tk.Label(root, text="Weather information will be displayed here.")

# Place widgets in the window
city_label.pack()
city_entry.pack()
get_weather_button.pack()
result_label.pack()

# Start the main loop
root.mainloop()