from django.test import Client
from django.urls import reverse
from rest_framework.test import APITestCase
from cart_app.models import Cart_item
import json

answer = (
    "Wireless Keyboard and Mouse has been added to your cart"
)



class Test_added_to_cart(APITestCase):
    fixtures = ["items.json"]

    def test_008_added_to_cart(self):
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
        response = self.client.post(
            reverse("an_item", args=[10])
        )
        with self.subTest():
            self.assertTrue(
                response.status_code == 201
                and len(Cart_item.objects.all()) == 1
            )
        self.assertEqual(json.loads(response.content), answer)
