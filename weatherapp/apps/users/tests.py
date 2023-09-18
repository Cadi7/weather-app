
from rest_framework import status
from rest_framework.test import APITestCase

from apps.users.models import User


class TestUserViews(APITestCase):

    def setUp(self):
        self.user_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'password': 'test123',
        }
        User.objects.create_user(self.user_data['email'], self.user_data['email'], self.user_data['password'])

    def test_register(self):
        user_data = {
            'first_name': 'Ccc',
            'last_name': 'Dd',
            'email': 'cristian@mail.com',
            'password': 'test123',
        }
        response = self.client.post('/api/users/register/', user_data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)

    def test_bad_register(self):
        response = self.client.post('/api/users/register/', {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'johnnel@@',
            'password': 'test123',
        })

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login(self):
        response = self.client.post('/api/users/login/', {
            'email': self.user_data['email'],
            'password': self.user_data['password'],
        })

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)

    def test_invalid_email(self):
        response = self.client.post('/api/users/login/', {
            'email': 'johnnel@@',
            'password': self.user_data['password'],
        })

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_invalid_password(self):
        response = self.client.post('/api/users/login/', {
            'email': self.user_data['email'],
            'password': 'wrongpassword',
        })

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn('error', response.data)




