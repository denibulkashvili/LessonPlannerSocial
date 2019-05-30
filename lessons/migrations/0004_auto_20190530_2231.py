# Generated by Django 2.2 on 2019-05-30 15:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0003_auto_20190524_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='author',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='content',
            field=models.TextField(blank=True, max_length=500, verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='lessons', related_query_name='lesson', to='lessons.Tag'),
        ),
    ]
