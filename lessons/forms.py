from django import forms
from .models import Lesson


class CreateLessonForm(forms.ModelForm):
    """Form to create new lesson plans"""

    class Meta:
        model = Lesson
        fields = (
            "title",
            "tags",
            "book",
            "lesson_number",
            "lesson_duration",
            "lesson_objectives",
            "resources",
            "content",
            "video_url",
        )
