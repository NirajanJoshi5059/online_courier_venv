from django.shortcuts import render
from product.forms import ProductForm

# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html')
    
def product_list(request):
    return render(request, 'product_list.html')

def product_form(request):
    # if request.POST:
    #     product_name=request.POST['product_name']
    #     print(product_name)
    form=ProductForm(request.POST or None)
    context={'form':form}
    return render(request, 'form.html',context)