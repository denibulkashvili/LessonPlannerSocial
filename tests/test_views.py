"""Module for testing views"""
from django.test import TestCase
from django.urls import reverse
import tests.testing_data as test_data


class HomePageTests(TestCase):
    """Tests home page"""

    def test_home_page_status_code(self):
        """Tests if homepage status code is 200"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_home_view_uses_correct_template(self):
        """Tests if homepage view uses index.html template"""
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "index.html")

    def test_home_page_contains_correct_header(self):
        """Tests if homepage contains Lesson Planner heading"""
        response = self.client.get(reverse("home"))
        self.assertContains(response, "Lesson Planner")


class AboutPageTests(TestCase):
    """Tests about page"""

    def test_about_page_status_code(self):
        """Tests if homepage status code is 200"""
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_about_view_uses_correct_template(self):
        """Tests if homepage view uses index.html template"""
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "about.html")

    def test_about_page_contains_correct_header(self):
        """Tests if homepage contains Lesson Planner heading"""
        response = self.client.get(reverse("about"))
        self.assertContains(response, "About")


class GamesPageTests(TestCase):
    """Tests games page"""

    def test_games_page_status_code(self):
        """Tests if games page status code is 200"""
        response = self.client.get("/games/")
        self.assertEqual(response.status_code, 200)

    def test_games_view_uses_correct_template(self):
        """Tests if games view uses index.html template"""
        response = self.client.get(reverse("games"))
        self.assertTemplateUsed(response, "games.html")

    def test_games_page_contains_correct_header(self):
        """Tests if games page contains Lesson Planner heading"""
        response = self.client.get(reverse("games"))
        self.assertContains(response, "Games")


class LessonListByUserTests(TestCase):
    """Tests LessonListByUser view"""

    def setUp(self):
        self.user = test_data.create_user()
        self.book = test_data.create_book()
        self.lesson = test_data.create_lesson(self.user, self.book)

    def test_lesson_list_by_user_page_status_code(self):
        """Tests if LessonListByUser view response status code is 200"""
        response = self.client.get(
            reverse("lessons:by_user", kwargs={"username": self.user.username})
        )
        self.assertEqual(response.status_code, 200)

    def test_lesson_list_by_user_page_uses_correct_template(self):
        """Tests if LessonListByUser view uses correct template"""
        response = self.client.get(
            reverse("lessons:by_user", kwargs={"username": self.user.username})
        )
        self.assertTemplateUsed(response, "lessons/lesson_list.html")

    def test_lesson_list_by_user_page_contains_lesson_by_this_user(self):
        """Test if LessonListByUser view contains a lesson create by this user"""
        response = self.client.get(
            reverse("lessons:by_user", kwargs={"username": self.user.username})
        )
        self.assertContains(response, self.user.username)
