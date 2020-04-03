from django.contrib import admin
from .models import MainPage, HomePageSlider, SliderImage
from .models import Address, UserProfile

class MainPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp', 'on_navigation')
    search_fields = ['title', 'sub_title', 'body']
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ["timestamp","updated"]

class SliderInline(admin.TabularInline):
    model = SliderImage
    extra = 0

class SliderAdmin(admin.ModelAdmin):
    inlines = [SliderInline]
    class Meta:
        model = HomePageSlider


class UserProfileAdmin(admin.ModelAdmin): 
    list_display = ( 'user', 'name', 'dob', 'active', 'staff')
    search_fields = ['user__username', 'gender', 'phone_number']

    class Meta:
    	model = UserProfile

    def name(self, obj):
        if obj.user.get_full_name():
            return obj.user.get_full_name()
        else:
    	    # return str(obj.user.first_name)+" "+ str(obj.user.last_name)
            return obj.fullname

class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'street_address',
        'state',
        'country',
        'zip_code',
        'default'
    ]
    list_filter = ['default', 'state', 'country']
    search_fields = ['user__user__username', 'street_address', 'state', 'zip_code']



# Register your models here.
admin.site.register(HomePageSlider, SliderAdmin)  
admin.site.register(MainPage, MainPageAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Address, AddressAdmin)