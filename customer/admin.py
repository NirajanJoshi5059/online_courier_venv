from django.contrib import admin
from customer.models import Customer, Gender

# Register your models here.

@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display=('gender_list',)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=('first_name', 'last_name', 'username')