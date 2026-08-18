from django.test import TestCase, Client
from django.urls import reverse


class Test_user_sign_up(TestCase):
    def test_001_user_sign_up(self):
        client = Client()
        response = client.post(
            reverse("signup"),
            data={"email": "fr@fr.com", "password": "fr"},
            content_type="application/json",
        )
        # print(response.content)
        with self.subTest():
            self.assertEqual(response.status_code, 201)
        self.assertTrue(
            b'{"client":"fr@fr.com"' in response.content
            and b"token" in response.content
        )
