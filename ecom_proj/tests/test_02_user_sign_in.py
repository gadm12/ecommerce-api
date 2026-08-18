from django.test import TestCase, Client
from django.urls import reverse


class Test_user_login_up(TestCase):
    def test_002_user_login_up(self):
        client = Client()
        client.post(
            reverse("signup"),
            data={"email": "fr@fr.com", "password": "fr"},
            content_type="application/json",
        )
        response = client.post(
            reverse("login"),
            data={"email": "fr@fr.com", "password": "fr"},
            content_type="application/json",
        )
        # print(response.content)
        with self.subTest():
            self.assertEqual(response.status_code, 200)
        self.assertTrue(
            b'"client":"fr@fr.com"' in response.content
            and b"token" in response.content
        )
