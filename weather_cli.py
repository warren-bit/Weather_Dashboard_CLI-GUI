import requests
import json
import os
from datetime import datetime
import argparse

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

def display_weather(data):
    if data:

        city = data['name']
        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        weather_desc = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        print("\n" + "=" * 40)
        print(f"    Weather in {city}, {country}:")
        print("=" * 40)
        print(f"Temperature: {temp}°C")
        print(f"Description: {weather_desc}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
        print("=" * 40 + "\n")

    else:
        print("No data to display.")

def save_history(city, data):
    entry = {
        "City": city,
        "timestamp": datetime.now().isoformat(),
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"]
    }
    
    file_name = "weather_history.json"
    history = []

# Load existing history if file exists
    if os.path.exists(file_name):
        with open(file_name, 'r') as file: 
            history = json.load(file)
    # Append new entry
    history.append(entry)

    # Save updated history
    with open(file_name, 'w') as file:
        json.dump(history, file, indent=4)
    
    print(f"Weather data for {city} saved to history.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch and display weather data for cities.")
    parser.add_argument("cities", nargs='*', help="City names to fetch weather for (optional)")
    parser.add_argument("-i", "--interactive", action="store_true", 
                        help="Force interactive mode even if cities are provided")

    args = parser.parse_args()

    # If cities are provided on command line AND not forcing interactive mode → batch mode
    if args.cities and not args.interactive:
        print("Fetching weather for provided cities...\n")
        for city in args.cities:
            print(f"Fetching weather data for {city}...")
            weather_data = get_weather_data(city)
            display_weather(weather_data)
            if weather_data:
                save_history(city, weather_data)
        print("\nAll done! Goodbye!")

    else:
        # Interactive mode (default when no cities given, or when -i is used)
        print("Welcome to Weather Dashboard!\n")
        print("Enter city names one at a time. Type 'quit' to exit.\n")

        while True:
            city = input("Enter city name (or 'quit' to exit): ").strip()

            if city.lower() == 'quit':
                print("\nThanks for using the weather app! Goodbye!")
                break

            if not city:
                print("Please enter a valid city name.\n")
                continue

            print(f"Fetching weather data for {city}...\n")
            weather_data = get_weather_data(city)
            display_weather(weather_data)
            if weather_data:
                save_history(city, weather_data)