import requests
from config import OPENWEATHERMAP_API_KEY
# import OPENWEATHERMAP_API_KEY from "config"


BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

def fetch_weather_data(city):
    params = {
        'q': 'Hamburg,DE',  # 'Hamburg' is the city name, and 'DE' is the country code for Germany.
        'appid': OPENWEATHERMAP_API_KEY,
        'units': 'metric'
    }


    response = requests.get(BASE_URL, params=params)
    data = response.json()

    return data
