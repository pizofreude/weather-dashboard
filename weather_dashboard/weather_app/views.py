# from django.shortcuts import render

# # Create your views here.
# views.py
from django.shortcuts import render
from .weather_fetcher import fetch_weather_data
from requests.exceptions import RequestException    # Handling errors


def weather_dashboard(request):
    # Replace 'Hamburg,DE' with the city you want to display weather data for.
    city = request.GET.get('city', 'Hamburg,DE')  # Default to Hamburg, Germany
    error_message = None    # Default error message is None

    try:
        # Attempt to fetch weather data
        weather_data = fetch_weather_data(city)

    except RequestException as e:
        # Handle API request error
        error_message = f"Error fetching weather data: {str(e)}"
        weather_data = None

    context = {
        'weather_data': weather_data,
        'city': city, # Pass the 'city' variable to the template.
        'error_message': error_message,
    }

    return render(request, 'weather_app/dashboard.html', context)

