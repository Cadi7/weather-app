from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from apps.users.models import User


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }


class TestWeatherViews(APITestCase):
    def setUp(self):
        self.user_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'password': 'test123',
        }

        self.user = User.objects.create_user(self.user_data['email'], self.user_data['email'],
                                             self.user_data['password'])
        token = get_tokens_for_user(self.user).get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")

    def test_current(self):
        response = self.client.get('/api/weather/current/')
        self.user.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('temperature', response.data)

    def test_search_location(self):
        location = 'Paris'
        response = self.client.get('/api/weather/search/?search_details={}'.format(location))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('location', response.data)
        self.assertIn('humidity', response.data)
        self.assertIn('Paris', response.data['location'])

    def test_search_zip(self):
        zip_code = '707267'
        response = self.client.get('/api/weather/search/?search_details={}'.format(zip_code))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('location', response.data)
        self.assertIn('humidity', response.data)
        self.assertIn('Iași', response.data['location'])

