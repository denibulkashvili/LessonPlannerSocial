"""Module for creating data for testing"""
from lessons.models import Lesson, Tag, Book
from accounts.models import User


def create_user():
    """Creates a test user"""
    return User.objects.create_user(
        username="test_model_user",
        email="test_model_user@mail.com",
        password="test123",
    )

def create_book():
    """Creates a test book"""
    return Book.objects.create(title="Test Book")

def create_tag():
    """Creates a test tag"""
    return Tag.objects.create(name="test tag")

def create_lesson(user, book):
    """Creates a test lesson"""
    lesson = Lesson.objects.create(
        title="Food lesson",
        author=user,
        book=book,
        lesson_number="33",
        lesson_duration=90,
        lesson_objectives="Learn about stuff",
        resources="Flashcards",
        content="1. Warm up",
        video_url="https://www.youtube.com/watch?v=tVlcKp3bWH8",
    )
    return lesson
