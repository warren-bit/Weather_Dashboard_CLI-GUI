import requests
import json
import os
from datetime import datetime
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox

API_KEY = os.getenv("WEATHER_API_KEY") # set your API_KEY environment variable: export WEATHER_API_KEY='your_api_key

if not API_KEY:
    print("ERROR: Please set your WEATHER_API_KEY environment variable.")
    exit()

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather_data(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        if response.status_code == 404:
            print("City not found. Check spelling!")
        elif response.status_code == 401:
            print("Invalid API key.")
        return None
    except requests.exceptions.RequestException as err:
        print(f"Error connecting to API: {err}")
        return None

def format_weather(data):
    if not data:
        return "No data to display."

    city = data['name']
    country = data["sys"]["country"]
    temp = data["main"]["temp"]
    weather_desc = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]

    output = "\n" + "=" * 40
    output += f"\n    Weather in {city}, {country}:"
    output += "=" * 40
    output += f"\nTemperature: {temp}°C"
    output += f"\nDescription: {weather_desc}"
    output += f"\nHumidity: {humidity}%"
    output += f"\nWind Speed: {wind_speed} m/s"
    output += "=" * 40 + "\n"
    return output

# GUI Application
def fetch_weather():
    city = entry.get().strip()
    if not city:
        messagebox.showwarning("Input Required", "Please enter a city name!")
        return
    
    status_label.config(text="Fetching weather...", foreground="blue")
    root.update()
    
    data = get_weather_data(city)
    
    if data:
        result = format_weather(data)
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, result)
        status_label.config(text=f"Weather for {city} loaded • {datetime.now().strftime('%H:%M:%S')}", foreground="green")
        # Optional: save to history if you want
    else:
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, f"❌ Could not fetch weather for '{city}'.\nCheck the city name or your internet connection.\n")
        status_label.config(text="Error fetching data", foreground="red")

# Create the main window
root = tk.Tk()
root.title("Weather Dashboard 🌍")
root.geometry("600x500")
root.resizable(True, True)
root.configure(bg="#f0f0f0")

# Title label
title_label = ttk.Label(root, text="Weather Dashboard", font=("Helvetica", 18, "bold"))
title_label.pack(pady=15)

# Input frame
input_frame = ttk.Frame(root)
input_frame.pack(pady=10)

entry = ttk.Entry(input_frame, width=40, font=("Helvetica", 12))
entry.pack(side=tk.LEFT, padx=5)
entry.focus()

button = ttk.Button(input_frame, text="Get Weather", command=fetch_weather)
button.pack(side=tk.LEFT, padx=5)

# Result area
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=20, font=("Consolas", 11), bg="white")
text_area.pack(pady=15, padx=20, fill=tk.BOTH, expand=True)

# Status bar
status_label = ttk.Label(root, text="Ready", relief=tk.SUNKEN, anchor=tk.W)
status_label.pack(side=tk.BOTTOM, fill=tk.X)

# Allow pressing Enter to fetch
root.bind('<Return>', lambda event: fetch_weather())

# Start the app
root.mainloop()  