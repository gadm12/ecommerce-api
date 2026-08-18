from django.test import Client
from django.urls import reverse
from rest_framework.test import APITestCase
import json

answer = {
    "cart_items": [
        {
            "id": 1,
            "item": {
                "id": 10,
                "category": "Other",
                "name": "Wireless Keyboard and Mouse",
                "price": "20.03",
            },
            "quantity": 1,
        },
        {
            "id": 2,
            "item": {
                "id": 9,
                "category": "Other",
                "name": "Code Editor Subscription",
                "price": "50.10",
            },
            "quantity": 1,
        },
        {
            "id": 3,
            "item": {
                "id": 3,
                "category": "Electronics",
                "name": "Lenovo ThinkPad",
                "price": "200.30",
            },
            "quantity": 2,
        },
        {
            "id": 4,
            "item": {
                "id": 5,
                "category": "Books",
                "name": "Cracking the Coding Interview",
                "price": "30.27",
            },
            "quantity": 1,
        },
    ],
    "total_price": 501.0,
}



class Test_decrease_cart_item(APITestCase):
    fixtures = ["items.json"]

    def test_012_decrease_cart_item(self):
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
        self.client.post(reverse("an_item", args=[9]))
        self.client.post(reverse("an_item", args=[3]))
        self.client.post(reverse("an_item", args=[5]))
        self.client.put(
            reverse("cart_item_quantity", args=["add", 3])
        )
        self.client.put(
            reverse("cart_item_quantity", args=["add", 3])
        )
        self.client.put(
            reverse("cart_item_quantity", args=["sub", 3])
        )
        response = self.client.get(reverse("cart"))
        # print(response.content)
        with self.subTest():
            self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), answer)
