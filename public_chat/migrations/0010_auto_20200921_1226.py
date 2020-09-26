# Generated by Django 2.2.15 on 2020-09-21 19:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('public_chat', '0009_auto_20200915_1321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publicchatroom',
            name='users',
        ),
        migrations.AddField(
            model_name='publicchatroom',
            name='users',
            field=models.ManyToManyField(help_text='users who are connected to chat room.', to=settings.AUTH_USER_MODEL),
        ),
    ]