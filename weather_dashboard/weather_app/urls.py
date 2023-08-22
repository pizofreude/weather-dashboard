from django.urls import path
from . import views  # Import your app's views

urlpatterns = [
    path('dashboard/', views.weather_dashboard, name='weather_dashboard'),  # Adjust or add more URL patterns as needed for the URL path as needed
]
