from django.urls import path
from django.contrib.auth.views import LogoutView
from useraccount.views import login_view, signup_view, UserLoginView
app_name='user'
urlpatterns=[
    path('',UserLoginView.as_view(), name='login'),
    path('register/',signup_view, name='signup'),
    path("logout/",LogoutView.as_view(), name='logout'),

    # path('send-email/', send_confirm_email, name='email'),
]