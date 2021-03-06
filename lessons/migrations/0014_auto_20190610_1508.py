# Generated by Django 2.2 on 2019-06-10 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("lessons", "0013_auto_20190610_1507")]

    operations = [
        migrations.AlterField(
            model_name="lesson",
            name="book",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="lessons",
                to="lessons.Book",
            ),
        )
    ]
