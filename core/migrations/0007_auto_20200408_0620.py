# Generated by Django 3.0.5 on 2020-04-08 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20200408_0535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
