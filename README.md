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
![GUI Screenshot](screenshots/gui_screenshot.png)

### CLI Version
![CLI Screenshot](screenshots/cli_output_screenshot.png)

## How to Use

### 1. Get an API Key
Sign up at [OpenWeatherMap](https://openweathermap.org/api) and get a free API key.

### 2. Set Your API Key
```bash
export WEATHER_API_KEY="your_actual_api_key_here"

3. Run the App
GUI Version (great for everyday use):
Bashpython weather_gui.py
CLI Version (perfect for scripting):
Bash# Interactive mode (default)
python weather_cli.py

# Batch mode: check multiple cities at once
python weather_cli.py Nairobi Tokyo London Paris
Installation
Bashgit clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name

# Optional: create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
Requirements

Python 3.6+
requests library
Tkinter (built-in; on Linux: sudo apt install python3-tk)

Project Structure
textyour-repo-name/
├── weather_cli.py         # Command-line version
├── weather_gui.py         # Graphical version
├── requirements.txt       # Dependencies
├── weather_history.json   # Auto-generated history (gitignored)
├── screenshots/           # Optional screenshots
├── .gitignore
└── README.md
Future Improvements

Add 5-day forecast
Weather icons in the GUI
Dark mode toggle
Package as a standalone executable

Made With ❤️ Using

Python
Requests
Tkinter
OpenWeatherMap API

Built by Warren — learning Python one project at a time! 🚀
Feel free to star ⭐, fork, or contribute!
text### Quick Checklist Before Pushing
1. Replace `yourusername/your-repo-name` with your actual repo URL.
2. Create a `screenshots` folder and add `gui.png` + `cli.png`.
3. Make sure `requirements.txt` exists (even if just `requests`).
4. Commit and push!

You’re all set — copy, paste, commit, push, and watch your repo shine!  

When it’s live, drop the link here. I’ll be first in line to give it a star! 🌟2.9sFast