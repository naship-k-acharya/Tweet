# Generated by Django 5.0.6 on 2024-09-22 11:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweet_beginner_app', '0004_friend_friendrequest'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friend',
            name='current_user',
        ),
        migrations.AlterField(
            model_name='friend',
            name='users',
            field=models.ManyToManyField(related_name='friends', to=settings.AUTH_USER_MODEL),
        ),
    ]
