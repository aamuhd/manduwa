# Generated by Django 3.0.5 on 2020-04-26 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20200410_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
    ]