# Generated by Django 5.0.3 on 2024-04-08 15:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_subscribe'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='subscribers',
            field=models.ManyToManyField(related_name='categories', through='news.Subscribe', to=settings.AUTH_USER_MODEL),
        ),
    ]
