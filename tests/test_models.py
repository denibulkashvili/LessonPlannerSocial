"""Module for testing models"""
from django.test import TestCase
from lessons.models import Lesson, Tag, Book
import tests.testing_data as test_data

# Create your tests here.
class LessonTestCase(TestCase):
    """Tests Lesson model"""

    @classmethod
    def setUpTestData(cls):
        """
        Run once to set up non-modified data for all class methods
        """
        user = test_data.create_user()
        book = test_data.create_book()
        test_data.create_lesson(user, book)

    def setUp(self):
        self.lesson = Lesson.objects.get(id=1)
        self.client.login(username="test_model_user", password="test123")

    def test_title_label(self):
        """Tests title field label"""
        field_label = self.lesson._meta.get_field("title").verbose_name
        self.assertEqual(field_label, "lesson title")

    def test_title_max_length(self):
        """Tests title field max length"""
        max_length = self.lesson._meta.get_field("title").max_length
        self.assertEqual(max_length, 200)

    def test_object_name_is_title(self):
        """Tests title ibject name"""
        expected_object_name = self.lesson.title
        self.assertEqual(expected_object_name, str(self.lesson))

    def test_get_absolute_url(self):
        """Test get_absolute_url method"""
        # This will also fail if the urlconf is not defined.
        self.assertEqual(
            self.lesson.get_absolute_url(), f"/lessons/id/{self.lesson.id}/"
        )

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
        """Tests lesson numebr field"""
        field_label = self.lesson._meta.get_field("lesson_number").verbose_name
        self.assertEqual(field_label, "lesson number")
        expected_object_name = self.lesson.lesson_number
        self.assertEqual(expected_object_name, "33")

    def test_lesson_duration_field(self):
        """Tests lesson duration field"""
        field_label = self.lesson._meta.get_field("lesson_duration").verbose_name
        self.assertEqual(field_label, "lesson duration (in minutes)")
        expected_object_name = self.lesson.lesson_duration
        self.assertEqual(expected_object_name, 90)

    def test_lesson_objectives_field(self):
        """Tests lesson objectives field"""
        field_label = self.lesson._meta.get_field("lesson_objectives").verbose_name
        max_length = self.lesson._meta.get_field("lesson_objectives").max_length
        self.assertEqual(field_label, "lesson objectives")
        self.assertEqual(max_length, 3000)
        expected_object_name = self.lesson.lesson_objectives
        self.assertEqual(expected_object_name, "Learn about stuff")

    def test_resources_field(self):
        """Tests lesson resources field"""
        field_label = self.lesson._meta.get_field("resources").verbose_name
        max_length = self.lesson._meta.get_field("resources").max_length
        self.assertEqual(field_label, "resources")
        self.assertEqual(max_length, 2000)
        expected_object_name = self.lesson.resources
        self.assertEqual(expected_object_name, "Flashcards")

    def test_content_field(self):
        """Tests lesson content field"""
        field_label = self.lesson._meta.get_field("content").verbose_name
        self.assertEqual(field_label, "content")
        expected_object_name = self.lesson.content
        self.assertEqual(expected_object_name, "1. Warm up")

    def test_video_url_field(self):
        """Tests lesson video url field"""
        field_label = self.lesson._meta.get_field("video_url").verbose_name
        max_length = self.lesson._meta.get_field("video_url").max_length
        self.assertEqual(field_label, "video link")
        self.assertEqual(max_length, 2000)
        expected_object_name = self.lesson.video_url
        self.assertEqual(
            expected_object_name, "https://www.youtube.com/watch?v=tVlcKp3bWH8"
        )

    def test_embed_video_url_parsed_correctly(self):
        """Test embed_video_url parsed correctly"""
        expected_object_name = self.lesson.embed_video_url
        self.assertEqual(
            expected_object_name, "https://www.youtube.com/embed/tVlcKp3bWH8"
        )


class TagTestCase(TestCase):
    """Tests Tag model"""

    @classmethod
    def setUpTestData(cls):
        test_data.create_tag()

    def setUp(self):
        self.tag = Tag.objects.get()

    def test_tag_name_field_label(self):
        """Test tag name field label"""
        field_label = self.tag._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "tag name")

    def test_tag_name_max_length(self):
        """Test tag name field ma length"""
        max_length = self.tag._meta.get_field("name").max_length
        self.assertEqual(max_length, 20)

    def test_slug_name(self):
        """Test tag slug name"""
        expected_slug_name = self.tag.slug
        split_n_join = lambda x: "-".join(x.split(" "))  # mimics slugify
        self.assertEqual(expected_slug_name, split_n_join(self.tag.name))

    def test_get_absolute_url(self):
        """Test tag get_absolute_url method"""
        self.assertEqual(
            self.tag.get_absolute_url(), f"/lessons/with-tag/{self.tag.slug}/"
        )


class BookTestCase(TestCase):
    """Tests Book model"""

    @classmethod
    def setUpTestData(cls):
        test_data.create_book()

    def setUp(self):
        self.book = Book.objects.get(id=1)

    def test_book_title_field_label(self):
        """Test book title field label"""
        field_label = self.book._meta.get_field("title").verbose_name
        self.assertEqual(field_label, "book title")

    def test_book_title_max_length(self):
        """Test book title field max length"""
        max_length = self.book._meta.get_field("title").max_length
        self.assertEqual(max_length, 100)

    def test_slug_name(self):
        """Test book slug field name"""
        expected_slug_name = self.book.slug
        split_n_join = lambda x: ("-".join(x.split(" "))).lower()
        self.assertEqual(expected_slug_name, split_n_join(self.book.title))

    def test_get_absolute_url(self):
        """Test book get_absolute_url method"""
        self.assertEqual(
            self.book.get_absolute_url(), f"/lessons/from-book/{self.book.slug}/"
        )
