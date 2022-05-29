from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from product.forms import ProductForm
from product.models import Product

# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html')
    
def product_list(request):
    products=Product.objects.all()
    context={'products':products}
    return render(request, 'product_list.html', context)

def product_form(request):
    # if request.POST:
    #     product_name=request.POST['product_name']
    #     print(product_name)
    form=ProductForm(request.POST or None)
    if form.is_valid():
        # print(form.cleaned_data)
        form.save()
        return HttpResponseRedirect(reverse('product:product_list'))
    context={'form':form}
    return render(request, 'form.html',context)

def edit_product(request, id):
    # product=Product.objects.get(id=id)
    product=get_object_or_404(Product, id=id)
    form=ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('product:product_list'))
    context={'form':form}
    return render(request, 'form.html', context)