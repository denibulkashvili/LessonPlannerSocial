# Generated by Django 2.2 on 2019-06-03 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("lessons", "0007_auto_20190602_0855")]

    operations = [
        migrations.AddField(
            model_name="lesson",
            name="is_featured",
            field=models.BooleanField(default=False),
        )
    ]
