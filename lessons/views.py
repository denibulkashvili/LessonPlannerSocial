from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.http import Http404
from django.contrib import messages
# from braces.views import SelectRelatedMixin

from django.views.generic import CreateView, DeleteView, DetailView, ListView
from lessons.models import Book, Lesson, Tag
from . import forms

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
class LessonListView(ListView):
    model = Lesson
    context_object_name = "lesson_list"

class LessonDetailView(DetailView):
    model = Lesson

class LessonListByUser(ListView):
    model = Lesson
    # template_name = "user_lesson_list.html"

    def get_queryset(self):
        try:
            self.lesson_author = User.objects.prefetch_related('lessons').get(username__iexact=self.kwargs.get('username'))
        except User.DoesNotExist:
            raise Http404
        else:
            return self.lesson_author.lessons.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["lesson_author"] = self.lesson_author  
        return context

class CreateLessonView(LoginRequiredMixin, CreateView):
    fields = ('title', 'tags', 'book', 'lesson_number', 'lesson_duration',
                'lesson_objectives', 'resources', 'content', 'video_url')    
    model = Lesson       

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)

class DeleteLessonView(LoginRequiredMixin, DeleteView):
    model = Lesson
    success_url = reverse_lazy("lessons:lesson_list")

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     return queryset.filter(author_id = self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Post deleted.")
        return super().delete(*args, **kwargs)
    

class TagListView(ListView):
    model = Tag
    context_object_name = "tag_list"

class TagDetailView(DetailView):
    model = Tag
    context_object_name = "tag_detail"

class BookListView(ListView):
    model = Book
    context_object_name = "book_list"

class BookDetailView(DetailView):
    model = Book
    context_object_name = "book_detail"
