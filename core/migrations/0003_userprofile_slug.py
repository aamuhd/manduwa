# Generated by Django 3.0.5 on 2020-04-07 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_mainpage_youtube_video_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='slug',
            field=models.SlugField(default='aliyu'),
            preserve_default=False,
        ),
    ]
