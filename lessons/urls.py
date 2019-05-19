from django.urls import path 
from . import views

app_name = "lessons"
 
urlpatterns = [
  path("all/", views.LessonListView.as_view(), name="lesson_list"), 
  path("id/<pk>/", views.LessonDetailView.as_view(), name="lesson_detail"),
  path("create/", views.CreateLessonView.as_view(), name="create"),
  path("delete/<pk>/", views.DeleteLessonView.as_view(), name="delete"),
  path("by/<username>/", views.LessonListByUser.as_view(), name="by_user"),
]
