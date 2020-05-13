from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from core.helpers import getUniqueId
from django_countries.fields import CountryField
from django.conf import settings
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.
class MainPage(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100, unique=True)
    sub_title = models.CharField(max_length=255, blank=True, null=True)
    img = models.ImageField(verbose_name="Main Image", blank=True, null=True, upload_to='images', help_text="Image size should be 922x731 px")
    body = RichTextUploadingField(blank=True, null=True)
    vid_file = models.FileField(upload_to='videos', blank=True, null=True, help_text="Upload Video File")
    extra_info = RichTextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now= False)
    updated = models.DateTimeField(auto_now_add=False, auto_now= True)
    on_navigation = models.BooleanField(default=False)

    class Meta: 
        verbose_name = 'Main Page'
        verbose_name_plural = 'Main Pages'
        ordering = ["-title", ]

   
    def __str__(self):
        return self.title


class HomePageSlider(models.Model):
    title = models.CharField(max_length=50)
    active = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now= False)
    updated = models.DateTimeField(auto_now_add=False, auto_now= True)    
    
    class Meta: 
        verbose_name = 'Home Page Slider'
        verbose_name_plural = 'Home Page Sliders'
        ordering = ["-updated", ]

    def __str__(self):
        return self.title

class SliderImage(models.Model):
    slider = models.ForeignKey(HomePageSlider, on_delete=models.CASCADE, related_name='sliders')
    file = models.ImageField(upload_to='images', help_text="Image size is 1900px width and 1267px height")
    header = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=300, blank=True, null=True)
    button = models.CharField(max_length=50, blank=True, null=True)
    button_url = models.CharField(max_length=100, blank=True, null=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now= True)
    class Meta: 
        verbose_name = 'Slider Image'
        verbose_name_plural = 'Slider Images'
        ordering = ["-updated", ]
    def __str__(self):
        return self.slider.title
 

GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Others', 'Others'),
)

class UserProfile(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    slug = models.SlugField()
    uid = models.CharField(default=getUniqueId, max_length=20, editable=False)
    fullname = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='profile_pics')
    dob = models.DateField(blank=True, null=True)
    phone_number = models.CharField(blank=True, null=True, max_length=15)
    work_email = models.EmailField(default='info@dabolinux.com') #TODO: fix here
    address = models.ForeignKey('core.Address', blank=True, null=True, on_delete=models.SET_NULL)
    bio = models.TextField(blank=True, null=True)
    gender = models.CharField(default="Others", blank=True, null=True, max_length=6, choices=GENDER)
    fb_link = models.URLField(blank=True, null=True)
    tw_link = models.URLField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    website_link  = models.URLField(blank=True, null=True)
    reg_date = models.DateTimeField(auto_now_add=True, auto_now= False)
    updated = models.DateTimeField(auto_now_add=False, auto_now= True)
    staff = models.BooleanField(default=False)
    active = models.BooleanField(default=False)

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "Users Profiles"
        ordering = ["-reg_date",]

    def get_absolute_url(self):
        # return reverse("model_detail", kwargs={"pk": self.pk})
        return '/jja/'
    

    def __str__(self):
        return f'{self.fullname}'




def userprofile_receiver(sender, instance, created, *args, **kwargs):
    if created:
        userprofile = UserProfile.objects.create(user=instance)
        userprofile.slug = userprofile.user.username
        userprofile.save()

post_save.connect(userprofile_receiver, sender=settings.AUTH_USER_MODEL)



class Address(models.Model):
    user = models.ForeignKey(UserProfile,
                             on_delete=models.CASCADE, related_name='addresses')
    street_address = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = CountryField(multiple=False)
    zip_code = models.CharField(max_length=100)
    default = models.BooleanField(default=False)


    class Meta:
        verbose_name_plural = 'Addresses'

    def __str__(self):
        return f'{self.user.user.username} - {self.street_address[:10]}' # self.user.user.username

    
    
