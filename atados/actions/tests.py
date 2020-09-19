from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import Action
from django.core.exceptions import ValidationError
from rest_framework.authtoken.models import Token


# Create your tests here.
class ActionTest(APITestCase):
    fixtures = ['users.json', 'actions.json']

    def setUp(self) -> None:
        token = Token.objects.get(user__username="davidgilmour")
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        self.valid_payload = {
            "name": "Levar gatinhos da rua para banho",
            "institute": "Abrigo Balio de Gato",
            "address": "Mossoró/RN",
            "description": "Dar apoio aos gatinhos da rua",
            "volunteer": [
                1,
                2,
                3
            ]
        }

        self.invalid_payload = {
            "name": "Levar gatinhos da rua para banho",
            "institute": "Abrigo Balio de Gato",
            "volunteer": [
                1,
                2,
                3
            ]
        }

    def test_create_valid_action(self):
        response = self.client.post('/api/actions/',
                                    data=self.valid_payload,
                                    format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_action(self):
        response = self.client.post('/api/actions/',
                                    data=self.invalid_payload,
                                    format='json')
        self.assertRaises(ValidationError)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
