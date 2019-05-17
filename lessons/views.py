from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView
from lessons.models import Book, Lesson, Tag

# Create your views here.
class CreateLessonView(LoginRequiredMixin, CreateView):
    fields = ('title', 'tags', 'book', 'lesson_number', 'lesson_duration',
                'lesson_objectives', 'resources', 'content', 'video_url')    
    model = Lesson       

class LessonListView(ListView):
    model = Lesson
    context_object_name = "lesson_list"

class LessonListByUser(ListView):
    model = Lesson
    context_object_name = "lesson_list"

class LessonDetailView(DetailView):
    model = Lesson
