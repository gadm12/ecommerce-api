from django.test import Client
from django.urls import reverse
from rest_framework.test import APITestCase
import json



answer = {
    "id": 10,
    "category": "Other",
    "name": "Wireless Keyboard and Mouse",
    "price": "20.03"
}



class Test_item_by_id(APITestCase):
    fixtures=["items.json"]

    def test_007_item_by_id(self):
        client = Client()
        sign_up_response = client.post(
            reverse("signup"),
            data={"email": "fr@fr.com", "password": "fr"},
            content_type="application/json",
        )
        response_body = json.loads(sign_up_response.content)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {response_body['token']}")
        response = self.client.get(reverse("an_item", args=[10]))
        with self.subTest():
            self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), answer)