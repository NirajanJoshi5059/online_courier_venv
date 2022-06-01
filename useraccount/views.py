from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from useraccount.forms import CustomSingupForm
from django.contrib.auth.views import LoginView, LogoutView

from django.template.loader import render_to_string
from django.core.mail import send_mail
# Create your views here.
def login_view(request):
    form=AuthenticationForm(request.POST or None)
    if request.POST:
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('product:product_list'))
    context={'form':form}
    return render(request, 'login.html', context)

class UserLoginView(LoginView):
    template_name='login.html'
    redirect_authenticated_user=True


def signup_view(request):
    form=CustomSingupForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('user:login'))
    context={'form':form}
    return render(request,'register.html', context)

def send_confirm_email(request):
    subject="Test Subject"
    message="Dummy Email"
    from_email="ytddash@gmail.com"
    recipient_list=['nirajanjoc19@gmail.com','kneerajun@gmail.com']
    html_message=render_to_string('email.html', {'name':'PYTHON'})
    result=send_mail(subject, message, from_email, recipient_list, html_message=html_message)
    return HttpResponse(result)