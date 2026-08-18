from django.test import Client
from django.urls import reverse
from rest_framework.test import APITestCase
import json


class Test_user_info(APITestCase):
    def test_003_user_info(self):
        client = Client()
        sign_up_response = client.post(
            reverse("signup"),
            data={"email": "fr@fr.com", "password": "fr"},
            content_type="application/json",
        )
        response_body = json.loads(sign_up_response.content)
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Token {response_body['token']}"
        )
        response = self.client.get(reverse("info"))
        with self.subTest():
            self.assertEqual(response.status_code, 200)
        self.assertTrue(
            b'{"email":"fr@fr.com"}' in response.content
        )
