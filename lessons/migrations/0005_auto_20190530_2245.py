# Generated by Django 2.2 on 2019-05-30 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0004_auto_20190530_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='content',
            field=models.TextField(max_length=500, verbose_name='content'),
        ),
    ]
