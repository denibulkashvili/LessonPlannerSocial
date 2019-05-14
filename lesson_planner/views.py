from django.views.generic import TemplateView, ListView
from lessons.models import Lesson

class HomePage(ListView):
    template_name = 'index.html'
    model = Lesson
    context_object_name = "lesson_list"

class TestPage(TemplateView):
    template_name = 'test.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class AboutPage(TemplateView):
    template_name = "about.html"

class GamesPage(TemplateView):
    template_name = "games.html"


