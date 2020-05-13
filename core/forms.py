from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = [
            'fullname', 'image', 'dob', 'phone_number', 'gender'
        ]