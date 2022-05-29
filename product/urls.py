from django.urls import path
from product.views import product_list,dashboard,product_form, edit_product


app_name='product'

urlpatterns=[
    path('product-list/', product_list, name='product_list'),
    path('',dashboard,name='dashboard'),
    path('save-product',product_form, name='product_form'),
    path('edit-product/<int:id>/', edit_product, name='edit_product'),
]