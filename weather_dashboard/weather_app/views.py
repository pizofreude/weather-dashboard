# from django.shortcuts import render

# # Create your views here.
# views.py
from django.shortcuts import render
from .weather_fetcher import fetch_weather_data

def weather_dashboard(request):
    # Replace 'Hamburg,DE' with the city you want to display weather data for.
    weather_data = fetch_weather_data('Hamburg,DE')

    context = {
        'weather_data': weather_data,
    }

    return render(request, 'weather_app/dashboard.html', context)

