# Generated by Django 3.0.5 on 2020-04-03 18:31

import ckeditor.fields
import ckeditor_uploader.fields
import core.helpers
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_address', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('zip_code', models.CharField(max_length=100)),
                ('default', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Addresses',
            },
        ),
        migrations.CreateModel(
            name='HomePageSlider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('active', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Home Page Slider',
                'verbose_name_plural': 'Home Page Sliders',
                'ordering': ['-updated'],
            },
        ),
        migrations.CreateModel(
            name='MainPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('sub_title', models.CharField(blank=True, max_length=255, null=True)),
                ('img', models.ImageField(blank=True, help_text='Image size should be 922x731 px', null=True, upload_to='images', verbose_name='Main Image')),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('vid_file', models.FileField(blank=True, help_text='Upload Video File', null=True, upload_to='videos')),
                ('youtube_video_id', models.CharField(blank=True, help_text='Youtube Video ID e.g L0I7i_lE5zA. Not Complete Url', max_length=20, null=True)),
                ('extra_info', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('on_navigation', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Main Page',
                'verbose_name_plural': 'Main Pages',
                'ordering': ['-title'],
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(default=core.helpers.getUniqueId, editable=False, max_length=20)),
                ('fullname', models.CharField(blank=True, max_length=50, null=True)),
                ('image', models.ImageField(blank=True, help_text='User Profile Picture', null=True, upload_to='profile_pics')),
                ('dob', models.DateField(blank=True, help_text='Date of Birth', null=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('work_email', models.EmailField(default='info@dabolinux.com', max_length=254)),
                ('bio', models.TextField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], default='Others', help_text='Gender', max_length=6, null=True)),
                ('fb_link', models.URLField(blank=True, null=True)),
                ('tw_link', models.URLField(blank=True, null=True)),
                ('github_link', models.URLField(blank=True, null=True)),
                ('instagram_link', models.URLField(blank=True, null=True)),
                ('linkedin_link', models.URLField(blank=True, null=True)),
                ('website_link', models.URLField(blank=True, null=True)),
                ('reg_date', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('staff', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=False)),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Address')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Profile',
                'verbose_name_plural': 'Users Profiles',
                'ordering': ['-reg_date'],
            },
        ),
        migrations.CreateModel(
            name='SliderImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(help_text='Image size is 1900px width and 1267px height', upload_to='images')),
                ('header', models.CharField(max_length=100)),
                ('sub_title', models.CharField(blank=True, max_length=300, null=True)),
                ('button', models.CharField(blank=True, max_length=50, null=True)),
                ('button_url', models.CharField(blank=True, max_length=100, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('slider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sliders', to='core.HomePageSlider')),
            ],
            options={
                'verbose_name': 'Slider Image',
                'verbose_name_plural': 'Slider Images',
                'ordering': ['-updated'],
            },
        ),
        migrations.AddField(
            model_name='address',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to='core.UserProfile'),
        ),
    ]
