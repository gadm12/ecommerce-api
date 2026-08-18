from django.test import Client
from django.urls import reverse
from rest_framework.test import APITestCase
import json
from cart_app.models import Cart_item


class Test_item_removed_from_cart(APITestCase):
    fixtures = ["items.json"]

    def test_009_item_removed_from_cart(self):
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
        self.client.post(reverse("an_item", args=[10]))
        response = self.client.delete(
            reverse("an_item", args=[10])
        )
        with self.subTest():
            self.assertEqual(len(Cart_item.objects.all()), 0)
        self.assertEqual(response.status_code, 204)
