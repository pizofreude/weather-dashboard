# Django Weather Dashboard

Welcome to the Django Weather Dashboard project. In this project, we've built a simple and interactive web application that allows users to check the current weather in various cities around the world.
This project involves usage of Big Data from `OpenWeatherMap API`.

## Table of Contents

- [Django Weather Dashboard](#django-weather-dashboard)
  - [Table of Contents](#table-of-contents)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [Project Overview](#project-overview)
    - [Features](#features)
    - [Screenshots](#screenshots)
  - [Usage](#usage)
    - [How to Use](#how-to-use)
    - [User Guide](#user-guide)
  - [Development](#development)
    - [Built With](#built-with)
    - [Directory Structure](#directory-structure)
  - [Deployment](#deployment)
  - [Contributing](#contributing)
  - [License](#license)

## Getting Started

### Prerequisites

Before you get started, make sure you have the following installed:

- Python (3.6 or higher)
- Django
- Git (optional, for version control)

### Installation

1. Clone this repository to your local machine (or download it):

```bash
git clone https://github.com/yourusername/weather-dashboard.git
```

2. Change to the project directory:

```bash
cd weather-dashboard
```

3. Install the required Python packages:

```bash
pip install -r requirements.txt
```

4. Set up your environment variables (See [Project Overview](#project-overview)).

5. Run the development server:

```bash
python manage.py runserver
```

6. Open a web browser and visit `http://localhost:8000/weather/dashboard` to see your weather dashboard in action!

## Project Overview

### Features

- Display current weather data for a user-specified city.
- Responsive and user-friendly interface.
- Error handling for invalid city names.
- User input for selecting a city to check the weather.
- Professional CSS styling for an appealing look.

### Screenshots

![Dashboard Screenshot 1](/screenshots/Day_24_3_0815.png)

![Dashboard Screenshot 2](/screenshots/Day_24_4_DOOM.png)

## Usage

### How to Use

1. Visit the application at `http://localhost:8000/weather/dashboard`.
2. Enter the name of the city you want to check the weather for.
3. Click the "Get Weather" button.
4. The dashboard will display the current temperature, humidity, and weather description for the specified city.

### User Guide

For a detailed guide on how to use the application and customize it, please refer to the [User Guide](/docs/user-guide.md).

## Development

### Built With

- Django - The web framework used.
- OpenWeatherMap API - For fetching weather data.
- HTML, CSS, and JavaScript - For front-end development.

### Directory Structure

- **weather_app**: Django app containing views, templates, and settings.
- **static**: Static files like CSS styles.
- **templates**: HTML templates for rendering views.
- **weather_fetcher.py**: Python script for fetching weather data.

## Deployment

This project is ready for deployment on platforms like Heroku, PythonAnywhere, or your preferred hosting provider. For detailed deployment instructions, please refer to the [Deployment Guide](/docs/deployment-guide.md).

## Contributing

Contributions are welcome! If you have ideas for improvements or new features, please open an issue or create a pull request. For major changes, please discuss them in advance.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.