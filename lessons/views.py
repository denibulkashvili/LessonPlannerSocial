"""Views for lesson app"""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import Http404
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from lessons.models import Book, Lesson, Tag
from .forms import (
    CreateBasicLessonForm,
    CreateArrowLessonForm,
    CreateBoomerangLessonForm,
    CreatePatchworkLessonForm,
)

User = get_user_model()  # pylint:disable=invalid-name

# pylint:disable=too-many-ancestors
# Create your views here.
class LessonListView(ListView):
    """Lesson list view"""

    model = Lesson
    context_object_name = "lesson_list"


class LessonDetailView(DetailView):
    """Lesson detail view"""

    model = Lesson


class LessonListByUser(ListView):
    """Lesson list by user view"""

    model = Lesson
    # template_name = "user_lesson_list.html"

    def get_queryset(self):  # pylint:disable=attribute-defined-outside-init
        try:
            self.lesson_author = User.objects.prefetch_related("lessons").get(
                username__iexact=self.kwargs.get("username")
            )
        except User.DoesNotExist:
            raise Http404
        else:
            return self.lesson_author.lessons.all()

    # pylint:disable=arguments-differ
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["lesson_author"] = self.lesson_author
        return context


class CreateBasicLessonView(LoginRequiredMixin, CreateView):
    """Create a Basic lesson view"""

    form_class = CreateBasicLessonForm
    model = Lesson
    template_name = "lessons/forms/lesson_form_basic.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.base = True
        self.object.save()
        return super().form_valid(form)


class CreateArrowLessonView(LoginRequiredMixin, CreateView):
    """Create an Arrow lesson view"""

    form_class = CreateArrowLessonForm
    model = Lesson
    template_name = "lessons/forms/lesson_form_arrow.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.arrow = True
        self.object.save()
        return super().form_valid(form)


class CreateBoomerangLessonView(LoginRequiredMixin, CreateView):
    """Create a Boomerang lesson view"""

    form_class = CreateBoomerangLessonForm
    model = Lesson
    template_name = "lessons/forms/lesson_form_boomerang.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.boomerang = True
        self.object.save()
        return super().form_valid(form)


class CreatePatchworkLessonView(LoginRequiredMixin, CreateView):
    """Create a Patchwork lesson view"""

    form_class = CreatePatchworkLessonForm
    model = Lesson
    template_name = "lessons/forms/lesson_form_patchwork.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.patchwork = True
        self.object.save()
        return super().form_valid(form)


class DeleteLessonView(LoginRequiredMixin, DeleteView):
    """Delete lesson view"""

    model = Lesson
    success_url = reverse_lazy("lessons:lesson_list")

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     return queryset.filter(author_id = self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Post deleted.")
        return super().delete(*args, **kwargs)


class UpdateLessonView(UpdateView):
    """Update Basic lesson view"""

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
    template_name = "lessons/forms/update_forms/lesson_update_basic.html"


class UpdateArrowLessonView(UpdateView):
    """Update Arrow lesson view"""

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
    template_name = "lessons/forms/update_forms/lesson_update_arrow.html"


class UpdateBoomerangLessonView(UpdateView):
    """Update Boomerang lesson view"""

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
    template_name = "lessons/forms/update_forms/lesson_update_boomerang.html"


class UpdatePatchworkLessonView(UpdateView):
    """Update Patchwork lesson view"""

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
    template_name = "lessons/forms/update_forms/lesson_update_patchwork.html"


class TagListView(ListView):
    """Tag list view"""

    model = Tag


class TagDetailView(DetailView):
    """Tag detail view"""

    model = Tag


class BookListView(ListView):
    """Book list view"""

    model = Book


class BookDetailView(DetailView):
    """Book detail view"""

    model = Book
