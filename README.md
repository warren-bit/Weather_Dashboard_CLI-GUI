# 🌍 Weather Dashboard

A beautiful and functional weather app built with Python — available in both **command-line** and **graphical (GUI)** versions.

Fetch real-time weather data for any city in the world using the OpenWeatherMap API.

## Features

- **Real-time weather** data (temperature, description, humidity, wind speed)
- Clean, formatted output with borders
- **CLI version**: Supports batch mode and interactive mode with history
- **GUI version**: Simple Tkinter window with input box and scrolling results
- Persistent history saved to `weather_history.json`
- Error handling for invalid cities and network issues
- Secure API key usage via environment variable

## Screenshots

### GUI Version
![GUI Screenshot](screenshots/gui.png)

### CLI Version
![CLI Screenshot](screenshots/cli.png)

## How to Use

### 1. Get an API Key
Sign up at [OpenWeatherMap](https://openweathermap.org/api) and get a free API key.

### 2. Set Your API Key
```bash
export WEATHER_API_KEY="your_actual_api_key_here
```

### 3. Run the App
**GUI Version** (great for everyday use):
```bash
python3 weather_gui.py
```
**CLI Version** (perfect for scripting):
- Iteractive mode(deafault):
```bash
python3 weather_cli.py
```
- Batch mode (check multiple cities at once):
```bash
python3 weather_cli.pi Nairobi Tokyo Paris
```

### Installation
```bash
git clone https://github.com/warren-bit/Weather_Dashboard_CLI-GUI.git
cd weather_Dashboard_CLI_GUI

# optional but recommended: Create a vvirtual environment
python -m venv venv
source venv/bin/activate      # On Windwos: venc/Scripys/activate

# install dependencies
pip install -r requirements.txt
```

### Requirements
- Python 3.6 or higher
- 'requests' library
- Tkinter (included in Python,; on Linux install with 'sudo apt install python3-tk' )

### Project Structure

Weather_Dashboard_CLI-GUI/
├── weather_cli.py         # Command-line version
├── weather_gui.py         # Graphical version
├── requirements.txt       # Project dependencies
├── weather_history.json   # Auto-generated history (gitignored)
├── screenshots/           # Optional screenshots
├── .gitignore
└── README.md

### Future Improvements
- Add 5-day forecast
- Display weather icons in the GUI
- Dark mode toggle
- Package as a standalone executable

### Made with ❤️ Using:
- Python
- Requsts
- Tkinter
- OpenWeatherMaop API

Built by **Warren** 🚀
Feel free to star ⭐, fork, or contribute!