# Generated by Django 2.2 on 2019-06-10 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0012_auto_20190609_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='activate_time',
            field=models.CharField(blank=True, default='0', max_length=10, verbose_name='activate time'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='activate_time2',
            field=models.CharField(blank=True, default='0', max_length=10, verbose_name='activate time'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='activate_time3',
            field=models.CharField(blank=True, default='0', max_length=10, verbose_name='activate time'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='engage_time',
            field=models.CharField(blank=True, default='0', max_length=10, verbose_name='engage time'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='engage_time2',
            field=models.CharField(blank=True, default='0', max_length=10, verbose_name='engage time'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='lesson_duration',
            field=models.IntegerField(blank=True, null=True, verbose_name='lesson duration (in minutes)'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='review_time',
            field=models.CharField(blank=True, default='0', max_length=10, verbose_name='review time'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='study_time',
            field=models.CharField(blank=True, default='0', max_length=10, verbose_name='study time'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='study_time2',
            field=models.CharField(blank=True, default='0', max_length=10, verbose_name='study time'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, related_name='lessons', related_query_name='lesson', to='lessons.Tag'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='wrap_up_time',
            field=models.CharField(blank=True, default='0', max_length=10, verbose_name='wrap up time'),
        ),
    ]
