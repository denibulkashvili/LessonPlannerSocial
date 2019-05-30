from django import forms
from .models import Lesson
from mediumeditor.widgets import MediumEditorTextarea

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
        widgets = {
            'content': MediumEditorTextarea(),
            'lesson_objectives': MediumEditorTextarea(),
            'resources': MediumEditorTextarea(),
        }

    