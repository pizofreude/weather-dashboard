# from django.shortcuts import render

# # Create your views here.
# views.py
from django.shortcuts import render
from .weather_fetcher import fetch_weather_data

def weather_dashboard(request):
    # Replace 'Hamburg,DE' with the city you want to display weather data for.
    city = request.GET.get('city', 'Hamburg,DE')  # Default to Hamburg, Germany
    weather_data = fetch_weather_data(city)

    context = {
        'weather_data': weather_data,
        'city': city, # Pass the 'city' variable to the template.
    }

    return render(request, 'weather_app/dashboard.html', context)

