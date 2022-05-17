from django.urls import path
from product.views import product_list


app_name='product'

urlpatterns=[
    path('product-list/', product_list, name='product_list'),
]