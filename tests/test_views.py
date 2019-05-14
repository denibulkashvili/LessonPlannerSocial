"""Module for testing views"""
from django.test import TestCase
from django.urls import reverse

class HomePageTests(TestCase):
    """Tests home page"""

    def test_home_page_status_code(self):
        """Tests if homepage status code is 200"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """Tests if homepage view uses index.html template"""
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "index.html")

    def test_home_page_contains_correct_header(self):
        """Tests if homepage contains Lesson Planner heading"""
        response = self.client.get(reverse("home"))
        self.assertContains(response, "Lesson Planner")
