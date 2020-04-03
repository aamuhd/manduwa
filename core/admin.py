from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'reg_time', 'active']
    list_filter = ['update', 'reg_time', 'active']


# Register your models here.
admin.site.register(UserProfile, UserProfileAdmin)