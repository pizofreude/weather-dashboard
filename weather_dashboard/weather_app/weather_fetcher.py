import requests
from . import config  # Import the 'config' module from the current package (app).

BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

def fetch_weather_data(city):
    params = {
        # 'q': 'Hamburg,DE',  # 'Hamburg' is the city name, and 'DE' is the country code for Germany.
        'q': f'{city}',  # Use the 'city' parameter passed to the function.
        'appid': config.OPENWEATHERMAP_API_KEY,  # Access the API key from the 'config' module.
        'units': 'metric'
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    return data

