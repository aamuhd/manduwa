from django.db import models
from django.conf import settings

# Create your models here.
GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Others', 'Others')
)
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(blank=True, null=True)
    fullname = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER)
    bio = models.TextField(blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    reg_time = models.DateTimeField(auto_now=True, auto_now_add=False)
    update = models.DateTimeField(auto_now=False, auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'Users Profile'
        ordering = ['-update']

    def __str__(self):
        if self.fullname:
            return f"{self.fullname}"
        else:
            return f"{self.user.username}"