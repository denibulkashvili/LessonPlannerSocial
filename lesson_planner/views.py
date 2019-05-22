from django.views.generic import TemplateView, ListView
from lessons.models import Lesson


class HomePage(ListView):
    template_name = "index.html"
    model = Lesson
    context_object_name = "lesson_list"


class HelloPage(TemplateView):
    template_name = "hello.html"


class GoodbyePage(TemplateView):
    template_name = "goodbye.html"


class AboutPage(TemplateView):
    template_name = "about.html"


class GamesPage(TemplateView):
    template_name = "games.html"
