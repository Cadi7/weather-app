from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.weather.views import WeatherView

router = DefaultRouter(trailing_slash=True,)
router.register(r'', WeatherView, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    *router.urls,
]
