"""Views for the Lesson Planner project"""
from django.views.generic import TemplateView, ListView
from lessons.models import Lesson
from django.contrib.auth.models import User


class HomePage(ListView):
    """Home page view"""
    template_name = "index.html"
    model = Lesson
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest"] = Lesson.objects.all()[:10]
        context["featured"] = Lesson.objects.filter(is_featured=True)
        context["num_users"] = User.objects.all().count()
        return context
    


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
