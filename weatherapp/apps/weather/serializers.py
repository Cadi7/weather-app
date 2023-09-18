from rest_framework import serializers


class WeatherSerializer(serializers.Serializer):
    day = serializers.CharField(required=False)
    location = serializers.CharField()
    temperature = serializers.FloatField()
    weather_description = serializers.CharField()
    humidity = serializers.FloatField()
    wind_speed = serializers.FloatField()


class SearchWeatherSerializer(serializers.Serializer):
    search_details = serializers.CharField()


class ForecastWeatherSerializer(serializers.Serializer):
    search_details = serializers.CharField(required=False)
