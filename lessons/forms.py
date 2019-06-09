"""Lesson forms module"""
from django import forms
from .models import Lesson


class CreateBaseLessonForm(forms.ModelForm):
    """Form to create new Base lesson plans"""
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

class CreateArrowLessonForm(forms.ModelForm):
    """Form to create new ESA Arrow lesson plans"""

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
            "video_url",
            # E-R-S-A-W
            "engage_time",
            "engage_description",
            "review_time",
            "review_description",
            "study_time",
            "study_description",
            "activate_time",
            "activate_description",
            "wrap_up_time",
            "wrap_up_description",
        )


class CreateBoomerangLessonForm(forms.ModelForm):
    """Form to create new ESA Boomerang lesson plans"""

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
            "video_url",
            # E-A-R-S-C-A2-W
            "engage_time",
            "engage_description",
            "activate_time",
            "activate_description",
            "review_time",
            "review_description",
            "study_time",
            "study_description",
            "activate_time2",
            "activate_description2",
            "wrap_up_time",
            "wrap_up_description",
        )

class CreatePatchworkLessonForm(forms.ModelForm):
    """Form to create new ESA Patchwork lesson plans"""

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
            "video_url",
            # E-R-A-A2-S-S2-E2-A3-W
            "engage_time",
            "engage_description",
            "review_time",
            "review_description",
            "activate_time",
            "activate_description",
            "activate_time2",
            "activate_description2",
            "study_time",
            "study_description",
            "engage_time2",
            "engage_description2",
            "activate_time3",
            "activate_description3",
            "wrap_up_time",
            "wrap_up_description",
        )
