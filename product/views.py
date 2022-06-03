from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from product.forms import ProductForm
from product.models import Product
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html')
    
def product_list(request):
    products=Product.objects.all()
    context={'products':products}
    return render(request, 'product_list.html', context)

class SaveProduct(LoginRequiredMixin, CreateView):
    model= Product
    form_class= ProductForm
    template_name= 'form.html'
    # login_url='user:login'

    def get_success_url(self):
        return reverse('product:product_list')
    
    def form_valid(self, form):
        product=form.save(commit=False)
        product.user=self.request.user
        return super().form_valid(product)
@login_required()
def save_product(request):
    # if request.POST:
    #     product_name=request.POST['product_name']
    #     print(product_name)
    form=ProductForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        # print(form.cleaned_data)
        product=form.save(commit=False)
        product.user=request.user
        product.save()
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