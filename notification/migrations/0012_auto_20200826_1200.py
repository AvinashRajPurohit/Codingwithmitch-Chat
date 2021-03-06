# Generated by Django 2.2.15 on 2020-08-26 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0011_notification_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='redirect_url',
            field=models.URLField(blank=True, help_text='The URL to be visited when a notification is clicked.', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='notification',
            name='image_url',
            field=models.URLField(blank=True, help_text='Thumbnail image for notification.', max_length=500, null=True),
        ),
    ]
