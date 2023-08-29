# User Guide

Welcome to the User Guide for the Django Weather Dashboard! In this guide, we'll walk you through the steps to use and customize the Weather Dashboard according to your preferences.

## Table of Contents

- [User Guide](#user-guide)
  - [Table of Contents](#table-of-contents)
  - [Using the Dashboard](#using-the-dashboard)
  - [Customizing the Dashboard](#customizing-the-dashboard)
    - [Changing the Default City](#changing-the-default-city)
    - [Modifying the Styles](#modifying-the-styles)
  - [Troubleshooting](#troubleshooting)
    - [Handling Invalid City Names](#handling-invalid-city-names)
    - [Error Messages](#error-messages)

## Using the Dashboard

1. **Accessing the Dashboard**: To access the Weather Dashboard, open a web browser and visit `http://localhost:8000/weather/dashboard` (or the URL where your application is hosted).

2. **Checking the Weather**:
   - On the dashboard, you'll see a text input field labeled "Enter City."
   - Type the name of the city you want to check the weather for in this input field.

3. **Getting Weather Data**:
   - After entering the city name, click the "Get Weather" button.
   - The dashboard will display the current temperature, humidity, and weather description for the specified city.

## Customizing the Dashboard

### Changing the Default City

By default, the Weather Dashboard displays weather information for Hamburg, Germany. You can easily change this default city to another location of your choice.

1. Open the `weather_dashboard/views.py` file in your project directory.

2. In the `weather_dashboard` function, find the line that sets the default city:

   ```python
   city = request.GET.get('city', 'Hamburg,DE')  # Default to Hamburg, Germany
   ```

3. Replace `'Hamburg,DE'` with the city and country code of your preferred default location. For example:

   ```python
   city = request.GET.get('city', 'Berlin,DE')  # Default to Berlin, Germany
   ```

4. Save the file.

### Modifying the Styles

You can modify the appearance of the Weather Dashboard by editing the CSS styles. Here's how:

1. Open the `weather_app/static/weather_app/styles.css` file.

2. Customize the CSS rules to change the colors, fonts, and layout as desired.

3. Save the file.

4. To see your style changes, you may need to refresh the dashboard in your web browser.

## Troubleshooting

### Handling Invalid City Names

- If you enter an invalid city name or a city not recognized by the weather API, the dashboard will display empty temperature, humidity, and weather description fields. You can customize this behavior in the `weather_dashboard/views.py` file under the "Error handling" section.

### Error Messages

- If there are any issues with fetching weather data, an error message will be displayed below the weather information. This message will provide information about the problem, such as API request errors.

If you encounter any issues not covered in this guide, please refer to the README or seek assistance from the project maintainers.

---

We hope you find this guide helpful in using and customizing the Django Weather Dashboard to suit your needs. If you have any questions or encounter difficulties, feel free to reach out for assistance.

Enjoy using the Weather Dashboard.

