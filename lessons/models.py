"""Models for lesson app"""
import uuid
from urllib import parse
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth import get_user_model


# Create your models here.
# pylint:disable=arguments-differ


class Lesson(models.Model):
    """Creates a Leson model"""

    title = models.CharField(
        max_length=200, verbose_name="lesson title", blank=False, default=""
    )
    author = models.ForeignKey(
        get_user_model(), related_name="lessons", on_delete=models.CASCADE, blank=True
    )
    created_at = models.DateField(auto_now=True)
    tags = models.ManyToManyField(
        "Tag", related_name="lessons", related_query_name="lesson", blank=True
    )
    book = models.ForeignKey(
        "Book", related_name="lessons", on_delete=models.CASCADE, blank=True, null=True
    )
    lesson_number = models.CharField(
        max_length=30, verbose_name="lesson number", default="", blank=True
    )
    lesson_duration = models.IntegerField(
        verbose_name="lesson duration (in minutes)", blank=True, null=True
    )
    ## TEXT FIELDS ##
    lesson_objectives = models.TextField(
        max_length=3000, verbose_name="lesson objectives", default="", blank=True
    )
    resources = models.TextField(
        max_length=2000, verbose_name="resources", default="", blank=True
    )
    video_url = models.CharField(
        max_length=2000, verbose_name="video link", default="", blank=True
    )
    embed_video_url = models.CharField(max_length=2000, editable=False, default="")
    is_featured = models.BooleanField(default=False)
    ## LESSON TEMPALTES ##
    base = models.BooleanField(default=False)
    arrow = models.BooleanField(default=False)
    boomerang = models.BooleanField(default=False)
    patchwork = models.BooleanField(default=False)
    ## CONTENT ##
    content = models.TextField(default="", blank=False)
    ### ESA TEMPLATES ###
    # Arrow = E-R-S-C-A-W,
    # Boomerang = E-A-R-S-C-A2-W,
    # Patchwork = E-R-A-A2-S-S2-C-E2-A3-W
    engage_time = models.CharField(
        max_length=10, verbose_name="engage time", blank=True, default="0"
    )
    engage_description = models.TextField(
        default="", verbose_name="engage description", blank=True
    )
    engage_time2 = models.CharField(
        max_length=10, verbose_name="engage time", blank=True, default="0"
    )
    engage_description2 = models.TextField(
        default="", verbose_name="engage description", blank=True
    )

    review_time = models.CharField(
        max_length=10, verbose_name="review time", blank=True, default="0"
    )
    review_description = models.TextField(
        default="", verbose_name="review description", blank=True
    )

    study_time = models.CharField(
        max_length=10, verbose_name="study time", blank=True, default="0"
    )
    study_description = models.TextField(
        default="", verbose_name="study description", blank=True
    )
    study_time2 = models.CharField(
        max_length=10, verbose_name="study time", blank=True, default="0"
    )
    study_description2 = models.TextField(
        default="", verbose_name="study description", blank=True
    )

    activate_time = models.CharField(
        max_length=10, verbose_name="activate time", blank=True, default="0"
    )
    activate_description = models.TextField(
        default="", verbose_name="activate description", blank=True
    )
    activate_time2 = models.CharField(
        max_length=10, verbose_name="activate time", blank=True, default="0"
    )
    activate_description2 = models.TextField(
        default="", verbose_name="activate description", blank=True
    )
    activate_time3 = models.CharField(
        max_length=10, verbose_name="activate time", blank=True, default="0"
    )
    activate_description3 = models.TextField(
        default="", verbose_name="activate description", blank=True
    )

    wrap_up_time = models.CharField(
        max_length=10, verbose_name="wrap up time", blank=True, default="0"
    )
    wrap_up_description = models.TextField(
        default="", verbose_name="wrap up description", blank=True
    )

    def get_embed_video_url(self):
        """Parses Youtube video url and formats a url for embed player"""
        try:
            video_url_parsed = parse.urlparse(self.video_url)
            qsl = parse.parse_qs(video_url_parsed.query)
            video_id = qsl["v"][0]
            self.embed_video_url = f"https://www.youtube.com/embed/{video_id}"
        except KeyError:
            print("Couldn't parse url. Check if url is a YouTube Video")

    def save(self, *args, **kwargs):
        self.get_embed_video_url()
        super(Lesson, self).save(*args, **kwargs)

    class Meta:
        ordering = ["-created_at"]
        indexes = [models.Index(fields=["title"])]
        # unique_together = ["author", "content"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Returns absolute url"""
        return reverse(
            "lessons:lesson_detail",
            kwargs={
                # "author":self.author.username,
                "pk": self.pk
            },
        )


class Tag(models.Model):
    """Creates a Tag model"""

    name = models.CharField(max_length=20, verbose_name="tag name")
    slug = models.SlugField(allow_unicode=True, unique=True, default=uuid.uuid1)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Method to get absolute url for a tag"""
        return reverse("lessons:tag_detail", kwargs={"slug": self.slug})


class Book(models.Model):
    """Creates a Book model"""

    title = models.CharField(max_length=100, verbose_name="book title")
    slug = models.SlugField(allow_unicode=True, unique=True, default=uuid.uuid1)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Book, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Method to get absolute url for a book"""
        return reverse("lessons:book_detail", kwargs={"slug": self.slug})

    class Meta:
        ordering = ["title"]
