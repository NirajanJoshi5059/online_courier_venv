from atexit import register
from django.contrib import admin
from useraccount.models import Gender, Profile
# Register your models here.

@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display=('gender_type',)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=('user','first_name','last_name','address','contact','profile_avatar',)

