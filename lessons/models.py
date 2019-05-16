from django.db import models
from django.urls import reverse

# Create your models here.

from django.contrib.auth import get_user_model
User = get_user_model()

class Lesson(models.Model):
    title = models.CharField(max_length=200, verbose_name="lesson title")
    author = models.ForeignKey(User, related_name="lessons", on_delete = models.CASCADE)
    created_at = models.DateField(auto_now=True)
    tags = models.ManyToManyField(
        "Tag", related_name="lessons", related_query_name="lesson"
    )
    book = models.ForeignKey("Book", related_name="lessons", on_delete = models.CASCADE)
    lesson_number = models.CharField(max_length=30, verbose_name="lesson number", default="")
    lesson_duration = models.IntegerField(
        verbose_name="lesson duration (in minutes)", default=0
    )
    lesson_objectives = models.TextField(
        max_length=500, verbose_name="lesson objectives", default=""
    )
    resources = models.TextField(max_length=500, verbose_name="resources", default="")
    content = models.TextField(max_length=500, verbose_name="content", default="")

    class Meta:
        ordering = ["-created_at"]
    def get_absolute_url(self):
        return reverse(
            "lessons:lesson_detail", kwargs={
                # "author":self.author.username,
                "pk":self.pk,
            }
        ) 


class Tag(models.Model):
    """Creates a Tag model"""

    name = models.CharField(max_length=20, verbose_name="tag name")
    slug = models.SlugField(allow_unicode=True, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("lessons:tag_detail", kwargs={"slug":self.slug})


class Book(models.Model):
    """Creates a Book model"""
    title = models.CharField(max_length=100, verbose_name="book title")
    slug = models.SlugField(allow_unicode=True, unique=True )

    def save(self, *args, **kwargs):
       self.slug = slugify(self.title)
       super(Book, self).save(*args, **kwargs)  

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("lessons:book_detail", kwargs={"slug":self.slug})

    class Meta:
        ordering = ["title"]
