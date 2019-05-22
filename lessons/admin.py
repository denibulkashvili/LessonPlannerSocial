"""Admin file fo lessons app"""
from django.contrib import admin
from .models import Book, Lesson, Tag

# Register your models here.
admin.site.register(Lesson)
admin.site.register(Tag)
admin.site.register(Book)
