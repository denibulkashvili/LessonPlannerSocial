"""Views for the Lesson Planner project"""
from django.views.generic import TemplateView, ListView
from lessons.models import Lesson


class HomePage(ListView):
    """Home page view"""
    template_name = "index.html"
    model = Lesson
    context_object_name = "lesson_list"


class HelloPage(TemplateView):
    """Successful login redirect page view"""
    template_name = "hello.html"


class GoodbyePage(TemplateView):
    """Logout redirect page view"""
    template_name = "goodbye.html"


class AboutPage(TemplateView):
    """About page view"""
    template_name = "about.html"


class GamesPage(TemplateView):
    """Games page view"""
    template_name = "games.html"
