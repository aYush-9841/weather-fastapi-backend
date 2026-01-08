# Weather API with FastAPI 🌦️

A backend service that fetches real-time weather data using the OpenWeather API.

## Features
- Get current weather by city name.
- Automatic Celsius conversion.
- Health advice based on temperature.
- Error handling for invalid city names.

## Setup Instructions
1. Clone the repository.
2. Create a virtual environment: `python -m venv venv`.
3. Install dependencies: `pip install -r requirements.txt`.
4. **API Key Setup:** - Create a `.env` file in the root directory.
   - Add your key: `OPENWEATHER_API_KEY=your_api_key_here`.

## How to Run
fastapi dev main.py 