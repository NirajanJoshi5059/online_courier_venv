from django.urls import path
from customer.views import customer_detail

app_name='customer'

urlpatterns=[
    path('customer-detail/',customer_detail, name='customer_detail'),
]