from django.test import Client
from django.urls import reverse
from rest_framework.test import APITestCase
import json



answer = [
    {
        "id": 1,
        "category": "Electronics",
        "name": "MacBook Pro",
        "price": "999.99"
    },
    {
        "id": 2,
        "category": "Electronics",
        "name": "Dell XPS 13",
        "price": "300.02"
    },
    {
        "id": 3,
        "category": "Electronics",
        "name": "Lenovo ThinkPad",
        "price": "200.30"
    },
    {
        "id": 7,
        "category": "Electronics",
        "name": "External Monitor",
        "price": "200.03"
    },
    {
        "id": 8,
        "category": "Electronics",
        "name": "Noise-Canceling Headphones",
        "price": "100.07"
    }
]



class Test_item_by_category(APITestCase):
    fixtures=["items.json"]

    def test_006_item_by_category(self):
        client = Client()
        sign_up_response = client.post(
            reverse("signup"),
            data={"email": "fr@fr.com", "password": "fr"},
            content_type="application/json",
        )
        response_body = json.loads(sign_up_response.content)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {response_body['token']}")
        response = self.client.get(reverse("items_by_category", args=['electronics']))
        with self.subTest():
            self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), answer)