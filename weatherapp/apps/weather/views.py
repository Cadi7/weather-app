import datetime

import geocoder
import requests
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from apps.weather.serializers import WeatherSerializer, SearchWeatherSerializer, ForecastWeatherSerializer

api_key = 'b588fdde62e72f353e97fbaa195daad3'


def extract_weather_data(data):
    temperature = data['main']['temp']
    weather_description = data['weather'][0]['description']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    location = data['name']

    weather_data = {
        'location': location,
        'temperature': temperature,
        'weather_description': weather_description,
        'humidity': humidity,
        'wind_speed': wind_speed
    }

    return weather_data


class WeatherView(GenericViewSet):
    serializer_class = WeatherSerializer

    def get_serializer_class(self):
        if self.action == "search_weather":
            return SearchWeatherSerializer
        return super().get_serializer_class()

    @action(methods=['GET'], detail=False, url_path='current')
    def user_weather(self, request):
        user_location = geocoder.ip('me').city
        user = request.user
        if user.location != user_location:
            user.location = user_location
            user.save()

        url = f'https://api.openweathermap.org/data/2.5/weather?q={user_location}&appid={api_key}&units=metric'
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            return Response({'error': 'An error occurred while fetching weather data'},
                            status=status.HTTP_400_BAD_REQUEST)

        weather_data = extract_weather_data(data)

        return Response(status=status.HTTP_200_OK, data=WeatherSerializer(weather_data).data)

    @action(methods=['GET'], detail=False, serializer_class=SearchWeatherSerializer, url_path='search')
    @swagger_auto_schema(query_serializer=SearchWeatherSerializer)
    def search_weather(self, request, **kwargs):
        search_details = request.query_params.get('search_details')

        url = f'https://api.openweathermap.org/data/2.5/weather?q={search_details}&appid={api_key}&units=metric'
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            return Response({'error': 'An error occurred while fetching weather data'},
                            status=status.HTTP_400_BAD_REQUEST)

        weather_data = extract_weather_data(data)

        serializer = WeatherSerializer(data=weather_data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(query_serializer=ForecastWeatherSerializer)
    @action(methods=['GET'], detail=False, url_path='forecast')
    def weather_forecast(self, request, **kwargs):
        search_details = request.query_params.get('search_details')
        user_location = geocoder.ip('me').city

        if search_details:
            url = f"https://api.openweathermap.org/data/2.5/forecast?q={search_details}&appid={api_key}&units=metric"
            user_location = search_details
        else:
            url = f"https://api.openweathermap.org/data/2.5/forecast?q={user_location}&appid={api_key}&units=metric"
            user_location = user_location

        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            return Response({'error': 'An error occurred while fetching weather data'},
                            status=status.HTTP_400_BAD_REQUEST)

        weather_list = []

        for forecast in data["list"]:
            dt_txt = forecast["dt_txt"]
            temp = forecast["main"]["temp"]
            weather_description = forecast["weather"][0]["description"]
            humidity = forecast["main"]["humidity"]
            wind_speed = forecast["wind"]["speed"]

            dt = datetime.datetime.strptime(dt_txt, "%Y-%m-%d %H:%M:%S")
            day = dt.strftime("%A") + " at " + dt.strftime("%H:%M")

            weather_data = {
                'location': user_location,
                'day': day,
                'temperature': temp,
                'weather_description': weather_description,
                'humidity': humidity,
                'wind_speed': wind_speed
            }
            weather_list.append(weather_data)

        serializer = WeatherSerializer(data=weather_list, many=True)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
