# Weather Application
This is a weather app that provides current weather information for a
user's location, allows users to search for weather in other locations, 
and displays a 7-day weather forecast. It utilizes Django Rest Framework
and integrates with the OpenWeatherMap API.

# Technologies used
- Python 3.11
- Docker
- Docker Compose
- PostgreSQL
- Django
- Django Rest Framework
- Swagger
- OpenWeatherMap API


# Features
- User Authentication: Users can create accounts and log in to access weather information.
- Current Weather: Displays the current weather for the user's location using the OpenWeatherMap API.
- Search Functionality: Allows users to search for weather in other locations by city name or zip code.
- Weather Forecast: Displays a 7-day weather forecast for the user's location or any searched location.
- API Endpoints: Provides the following API endpoints:
```/api/weather/current/: Returns current weather for the user's location.
/api/weather/search/: Takes a city name or zip code and returns weather information for that location.
/api/weather/forecast/: Returns a 7-day weather forecast for the user's location or any searched location.
```
- Error Handling: Gracefully handles errors and returns appropriate error messages to the user.
- Documentation: Proper documentation is available for the API endpoints and their usage.
- Testing: Unit tests are included for each API endpoint to ensure correct functionality.
- Dockerized: The project is Dockerized for easy setup and deployment.
- PostgreSQL: Utilizes a PostgreSQL database connection.


# Prerequisites

Before you begin, ensure you have the following prerequisites installed:

- Python 3.11
- Docker

# Installation and Setup
1. Clone the repository to your local machine:
```bash
git clone https://github.com/cadi7/weather-app.git
cd weather-app
```

2. Build and start the Docker containers using Docker Compose:
```bash
docker-compose up
```
This command will create and run the containers for the application and the PostgreSQL database.

*(If the migrations are not created, use `python manage.py makemigrations` && `python manage.py migrate` in the Docker container console.)*

3. Access the application in your web browser using the address http://localhost:8000


# Usage
- Create an account and log in to access weather information. _(Set Bearer Token in available authorizations)_
- Use the /api/weather/current/ endpoint to get the current weather for your location.
- Use the /api/weather/search/ endpoint with a city name or zip code to search for weather information in other locations.
- Access the /api/weather/forecast/ endpoint to view a 5-day weather forecast for your location or any searched location.

*In case you don't want to use the interface, you can directly use the server link.*

**You can see more details for the use of endpoints in the 'Documentation' folder.**