from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
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
    form=ProductForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        # print(form.cleaned_data)
        form.save()
        return HttpResponseRedirect(reverse('product:product_list'))
    context={'form':form}
    return render(request, 'form.html',context)

def edit_product(request, id):
    # product=Product.objects.get(id=id)
    product=get_object_or_404(Product, id=id)
    form=ProductForm(request.POST or None, request.FILES or None, instance=product)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('product:product_list'))
    context={'form':form}
    return render(request, 'form.html', context)

def delete_product(request, id):
    # product=get_object_or_404(Product, id=id)
    try:
        product=Product.objects.get(id=id)
    except Product.DoesNotExist:
        return HttpResponse("Product doesn't found.")
    product.delete()
    return HttpResponseRedirect(reverse('product:product_list'))
    # return HttpResponseRedirect('product/delete-product/product.id')