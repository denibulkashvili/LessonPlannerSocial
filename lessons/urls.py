"""Urls file for lessons app"""
from django.urls import path
from . import views

app_name = "lessons"

urlpatterns = [
    path("all/", views.LessonListView.as_view(), name="lesson_list"),
    path("id/<pk>/", views.LessonDetailView.as_view(), name="lesson_detail"),
    path("create/", views.CreateLessonView.as_view(), name="create"),
    path("delete/<pk>/", views.DeleteLessonView.as_view(), name="delete"),
    path("update/<pk>/", views.UpdateLessonView.as_view(), name="update"),
    path("by/<username>/", views.LessonListByUser.as_view(), name="by_user"),
    path("with-tag/all/", views.TagListView.as_view(), name="tag_list"),
    path("with-tag/<slug:slug>/", views.TagDetailView.as_view(), name="tag_detail"),
    path("from-book/all/", views.BookListView.as_view(), name="book_list"),
    path("from-book/<slug:slug>/", views.BookDetailView.as_view(), name="book_detail"),
]
