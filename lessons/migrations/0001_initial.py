# Generated by Django 2.2 on 2019-05-08 03:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='book title')),
                ('slug', models.SlugField(allow_unicode=True, unique=True)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='tag name')),
                ('slug', models.SlugField(allow_unicode=True, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='lesson title')),
                ('created_at', models.DateField(auto_now=True)),
                ('lesson_number', models.CharField(default='', max_length=30, verbose_name='lesson number')),
                ('lesson_duration', models.IntegerField(default=0, verbose_name='lesson duration (in minutes)')),
                ('lesson_objectives', models.TextField(default='', max_length=500, verbose_name='lesson objectives')),
                ('resources', models.TextField(default='', max_length=500, verbose_name='resources')),
                ('content', models.TextField(default='', max_length=500, verbose_name='content')),
                ('content_html', models.TextField(editable=False)),
                ('video_url', models.CharField(default='', max_length=200, verbose_name='video link')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to=settings.AUTH_USER_MODEL)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='lessons.Book')),
                ('tags', models.ManyToManyField(related_name='lessons', related_query_name='lesson', to='lessons.Tag')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddIndex(
            model_name='lesson',
            index=models.Index(fields=['title'], name='lessons_les_title_6beb42_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='lesson',
            unique_together={('author', 'content')},
        ),
    ]
