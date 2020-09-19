from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import User
from django.core.exceptions import ValidationError
from rest_framework.authtoken.models import Token


# Create your tests here.
class ClientManagerTest(APITestCase):

    fixtures = ['users.json']

    def setUp(self) -> None:

        token = Token.objects.get(user__username="davidgilmour")
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        self.valid_payload = {
            'first_name': 'Japeto',
            'last_name': 'Japeto',
            'email': 'japetolunar@saturn.com',
            'username': 'japetolunar',
            'district': 'Abolição 3',
            'city': 'Mossoró/RN',
            'password': 'test1234'
        }

        self.invalid_payload = {
            'name': 'Discovery Lunar',
            'cpf': '89198119460',
            'username': 'discoverylunar',
            'password': 'test1234'
        }

    def test_authentication(self):
        response = self.client.post('/api-token-auth/',
                                    data={'username': 'johnlennon', 'password': 'test1234'},
                                    format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_authentication(self):
        response = self.client.post('/api-token-auth/',
                                    data={'username': 'johnlennon', 'password': 'test12345'},
                                    format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_valid_user(self):
        response = self.client.post('/api/users/',
                                    data=self.valid_payload,
                                    format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_user(self):
        response = self.client.post('/api/users/',
                                    data=self.invalid_payload,
                                    format='json')
        self.assertRaises(ValidationError)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
