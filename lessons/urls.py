from django.urls import path 
from . import views

app_name = "lessons"
 
urlpatterns = [
  path("all/", views.LessonListView.as_view(), name="lesson_list"), 
  path("id/<pk>/", views.LessonDetailView.as_view(), name="lesson_detail"),
  path("create/", views.CreateLessonView.as_view(), name="create"),
  # path("by_user/<username:username>/", views.LessonListByUser.as_view(), name="by_user"),
  path("tags/", views.TagListView.as_view(), name="tag_list"),
  path("tag/<slug:slug>", views.TagDetailView.as_view(), name="tag_detail"),
  path("books/", views.BookListView.as_view(), name="book_list"),
  path("book/<slug:slug>", views.BookDetailView.as_view(), name="book_detail"),
]
