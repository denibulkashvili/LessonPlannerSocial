"""Views for the Lesson Planner project"""
from django.views.generic import TemplateView, ListView
from django.contrib.auth.models import User
from django.db.models import Count
from lessons.models import Lesson, Tag


class HomePage(ListView):
    """Home page view"""
    template_name = "index.html"
    model = Lesson

    @staticmethod
    def get_popular_tags():
        """Gets a list of tags ordered by most amount of lessons"""
        all_tags = Tag.objects.all()
        ordered_tags = all_tags.annotate(num_lessons=Count('lesson')).order_by('-num_lessons')
        return ordered_tags[:5]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest"] = Lesson.objects.all()[:10]
        context["featured"] = Lesson.objects.filter(is_featured=True)
        context["num_users"] = User.objects.all().count()
        context["popular_tags"] = self.get_popular_tags()
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
