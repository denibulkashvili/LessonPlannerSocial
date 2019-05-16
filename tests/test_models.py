from django.test import TestCase
from lessons.models import Lesson, Tag, Book
from accounts.models import User

# Create your tests here.
class LessonTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        Run once to set up non-modified data for all class methods
        """
        user = User.objects.create_user(username="test_model_user", email="test_model_user@mail.com", password="test123")
        book = Book.objects.create(title="Test Book")
        Lesson.objects.create(
            title="Food lesson", 
            book=book, 
            author=user, 
            lesson_number="33",
            lesson_duration=90,
            lesson_objectives="Learn about stuff",
            resources="Flashcards",
            content="1. Warm up",
            video_url="https://www.youtube.com/watch?v=tVlcKp3bWH8",
        )

    def setUp(self):
        self.lesson = Lesson.objects.get(id=1)
        self.client.login(username='test_model_user', password='test123')

    def test_title_label(self):
        field_label = self.lesson._meta.get_field("title").verbose_name
        self.assertEqual(field_label, "lesson title")

    def test_title_max_length(self):
        max_length = self.lesson._meta.get_field("title").max_length
        self.assertEqual(max_length, 200)

    def test_object_name_is_title(self):
        expected_object_name = self.lesson.title
        self.assertEqual(expected_object_name, str(self.lesson))

    def test_get_absolute_url(self):
        # This will also fail if the urlconf is not defined.
        self.assertEqual(self.lesson.get_absolute_url(), f"/lessons/id/{self.lesson.id}/")

    def test_author_field(self):
        """Test post author field"""
        field_label = self.lesson._meta.get_field("author").verbose_name
        self.assertEqual(field_label, "author")
        expected_object_name = self.lesson.author.username
        self.assertEqual(expected_object_name, "test_model_user")

    def test_lesson_tags_field(self):
        """Tests tags field in Post"""
        field_label = self.lesson._meta.get_field("tags").verbose_name
        self.assertEqual(field_label, "tags")

    def test_lesson_can_query_tags_through_tags_field(self):
        """Tests if Lesson can query related tags"""
        tag = Tag.objects.create(name="test tag")
        self.lesson.tags.add(tag)
        self.assertEqual(self.lesson.tags.get(id=1), tag)

    def test_lesson_book_field(self):
        """Tests book field in Post"""
        field_label = self.lesson._meta.get_field("book").verbose_name
        self.assertEqual(field_label, "book")

    def test_lesson_can_query_book(self):
        """Tests if Lesson can query related book"""
        self.assertEqual(self.lesson.book.title, "Test Book")

    def test_lesson_number_field(self):
        field_label = self.lesson._meta.get_field("lesson_number").verbose_name
        self.assertEqual(field_label, "lesson number")
        expected_object_name = self.lesson.lesson_number
        self.assertEqual(expected_object_name, "33")

    def test_lesson_duration_field(self):
        field_label = self.lesson._meta.get_field("lesson_duration").verbose_name
        self.assertEqual(field_label, "lesson duration (in minutes)")
        expected_object_name = self.lesson.lesson_duration
        self.assertEqual(expected_object_name, 90)

    def test_lesson_objectives_field(self):
        field_label = self.lesson._meta.get_field("lesson_objectives").verbose_name
        max_length = self.lesson._meta.get_field("lesson_objectives").max_length
        self.assertEqual(field_label, "lesson objectives")
        self.assertEqual(max_length, 500)
        expected_object_name = self.lesson.lesson_objectives
        self.assertEqual(expected_object_name, "Learn about stuff")

    def test_resources_field(self):
        field_label = self.lesson._meta.get_field("resources").verbose_name
        max_length = self.lesson._meta.get_field("resources").max_length
        self.assertEqual(field_label, "resources")
        self.assertEqual(max_length, 500)
        expected_object_name = self.lesson.resources
        self.assertEqual(expected_object_name, "Flashcards")

    def test_content_field(self):
        field_label = self.lesson._meta.get_field("content").verbose_name
        self.assertEqual(field_label, "content")
        expected_object_name = self.lesson.content
        self.assertEqual(expected_object_name, "1. Warm up")

    def test_video_url_field(self):
        field_label = self.lesson._meta.get_field("video_url").verbose_name
        max_length = self.lesson._meta.get_field("video_url").max_length
        self.assertEqual(field_label, "video link")
        self.assertEqual(max_length, 2000)
        expected_object_name = self.lesson.video_url
        self.assertEqual(expected_object_name, "https://www.youtube.com/watch?v=tVlcKp3bWH8")

    def test_embed_video_url_parsed_correctly(self):
        expected_object_name = self.lesson.embed_video_url
        self.assertEqual(expected_object_name, "https://www.youtube.com/embed/tVlcKp3bWH8")
