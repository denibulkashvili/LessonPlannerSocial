# Generated by Django 2.2 on 2019-06-02 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("lessons", "0006_auto_20190530_2246")]

    operations = [
        migrations.AlterField(
            model_name="lesson", name="content", field=models.TextField(default="")
        ),
        migrations.AlterField(
            model_name="lesson",
            name="lesson_objectives",
            field=models.TextField(
                blank=True,
                default="",
                max_length=3000,
                verbose_name="lesson objectives",
            ),
        ),
        migrations.AlterField(
            model_name="lesson",
            name="resources",
            field=models.TextField(
                blank=True, default="", max_length=2000, verbose_name="resources"
            ),
        ),
    ]
