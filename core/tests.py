from django.test import TestCase
from django.urls import reverse


class CorePageTests(TestCase):

    def test_home_page_returns_200(self):
        response = self.client.get(
            reverse("core:home"),
            secure=True,
        )
        self.assertEqual(response.status_code, 200)

    def test_case_study_page_returns_200(self):
        response = self.client.get(
            reverse("core:careertrack_case_study"),
            secure=True,
        )
        self.assertEqual(response.status_code, 200)