# Deployment Guide

This guide will walk you through the process of deploying the Django Weather Dashboard to a hosting service. We'll use [PythonAnywhere](https://www.pythonanywhere.com/) as an example hosting platform, which offers a free tier suitable for small projects like this one.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Deployment Steps](#deployment-steps)
- [Running the Application](#running-the-application)

## Prerequisites

Before you begin, make sure you have the following:

- A [PythonAnywhere](https://www.pythonanywhere.com/) account (free tier is sufficient).
- [Git](https://git-scm.com/) installed on your local machine.
- The [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) installed (for the Heroku alternative, if desired).

## Deployment Steps

### Step 1: Clone the Repository

1. Open your terminal or command prompt.

2. Navigate to the directory where you want to store your project (e.g., your user directory).

3. Clone your Weather Dashboard repository from GitHub:

   ```bash
   git clone https://github.com/your-username/weather-dashboard.git
   ```

   Replace `your-username` with your GitHub username.

### Step 2: Set Up PythonAnywhere

1. Log in to your [PythonAnywhere](https://www.pythonanywhere.com/) account.

2. From the dashboard, click on "Files" to open the file explorer.

3. Navigate to the directory where you cloned your repository.

4. Create a new virtual environment for your project. In the terminal, run:

   ```bash
   mkvirtualenv --python=/usr/bin/python3.8 myenv
   ```

   Replace `myenv` with your preferred virtual environment name.

5. Activate the virtual environment:

   ```bash
   workon myenv
   ```

6. Install project dependencies using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

### Step 3: Configure Environment Variables

1. In PythonAnywhere, go to the "Web" tab.

2. Click on your web app's domain name to open its configuration page.

3. Under the "Virtualenv" section, set the path to your virtual environment, like `/home/your-username/.virtualenvs/myenv`.

4. In the "WSGI configuration file" section, add the following lines to the bottom of the file (replace `your-username` with your actual username):

   ```bash
   import os
   import sys

   path = '/home/your-username/weather-dashboard'
   if path not in sys.path:
       sys.path.append(path)

   os.environ['DJANGO_SETTINGS_MODULE'] = 'weather_dashboard.settings'

   from django.core.wsgi import get_wsgi_application
   application = get_wsgi_application()
   ```

### Step 4: Database Setup

1. In PythonAnywhere, go to the "Databases" tab (available in paid accounts) if you need a database. You can also use a remote database service like [Heroku Postgres](https://www.heroku.com/postgres) or [ElephantSQL](https://www.elephantsql.com/) for free.

2. Configure your `settings.py` to use the database you've set up. Update the `DATABASES` setting accordingly.

### Step 5: Collect Static Files

1. Run the following command to collect static files (CSS, JavaScript, etc.):

   ```bash
   python manage.py collectstatic
   ```

### Step 6: Run Migrations

1. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

### Step 7: Create a Superuser (Optional)

1. If you want to access the Django admin panel, create a superuser:

   ```bash
   python manage.py createsuperuser
   ```

### Step 8: Finalize Deployment

1. From the PythonAnywhere dashboard, go to the "Web" tab.

2. Click the "Reload" button to apply your changes.

## Running the Application

1. Visit your hosted application in a web browser by navigating to your PythonAnywhere domain or custom domain if you have one.

2. You should now see the Weather Dashboard. Enter a city name and click "Get Weather" to view weather information.

Congratulations! You have successfully deployed the Django Weather Dashboard.

