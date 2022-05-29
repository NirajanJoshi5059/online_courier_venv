from django.shortcuts import render
from customer.forms import CustomerForm

# Create your views here.
def customer_detail(request):
    form=CustomerForm(request.POST or None)
    context={'form':form}
    return render(request, 'customerform.html', context)