# Generated by Django 5.1.6 on 2025-02-20 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_car_audio_car_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='audio',
            new_name='video',
        ),
    ]
