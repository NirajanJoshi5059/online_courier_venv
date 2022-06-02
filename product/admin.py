from django.contrib import admin
from product.models import Product, Weight
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=('name','price','quantity','status','weight','created','modified',)
    # list_filter=('status',)

@admin.register(Weight)
class WeightAdmin(admin.ModelAdmin):
    list_display=('weight_range','price',)

