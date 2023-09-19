from django.shortcuts import render,redirect
from .models import Product, Category
from .forms import ProductForm, CategoryForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.auth import admin_only

# Create your views here.
@login_required
@admin_only
def index(request):
    # fetch data from the table
    products=Product.objects.all()
    context={
        'products':products
    }
    # render- page load garni
    return render(request,'products/products.html',context)

@login_required
@admin_only
def post_product(request):
    if request.method =='POST':
        forms=ProductForm(request.POST,request.FILES)
        if forms.is_valid():
            forms.save()
            messages.add_message(request, messages.SUCCESS, 'product added')
            return redirect('/products/addproduct')
        else:
            messages.add_message(request, messages.ERROR,'failed to add product')
            return render(request,'products/addproduct.html',{'forms':forms})
        
    context={
        'forms':ProductForm
    }
    return render(request, 'products/addproduct.html',context)

@login_required
@admin_only
def update_product(request, product_id):
    instance=Product.objects.get(id=product_id) 
    if request.method=="POST":
        forms=ProductForm(request.POST, request.FILES, instance=instance)
        if forms.is_valid():
            forms.save()
            messages.add_message(request, messages.SUCCESS, 'product updated')
            return redirect('/products')
        else:
            messages.add_message(request, messages.ERROR,'failed to update project')
            return render(request,'products/updateproduct.html',{'forms':forms})
        
    context={
        'forms':ProductForm(instance=instance)
    }
    return render(request, 'products/updateproduct.html',context)

@login_required
@admin_only
def delete_product(request, product_id):
    product=Product.objects.get(id=product_id)
    product.delete()
    messages.add_message(request, messages.SUCCESS, "product deleted")
    return redirect("/products")
       
@login_required
@admin_only      
def post_category(request):
    if request.method =='POST':
        forms=CategoryForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.add_message(request, messages.SUCCESS, 'category added')
            return redirect('/products/addcategory')
        else:
            messages.add_message(request, messages.ERROR,'failed to add category')
            return render(request,'products/addcategory.html',{'forms':forms})
        
    context={
        'forms':CategoryForm
    }
    return render(request, 'products/addcategory.html',context)

    # fetch data from the table
@login_required
@admin_only
def show_category(request):
    # fetch data from the table
    categories=Category.objects.all()
    context={
        'categories':categories
    }
    # render- page load garni
    return render(request,'products/category.html',context)

@login_required
@admin_only
def update_category(request, category_id):
    instance=Category.objects.get(id=category_id) 
    if request.method=="POST":
        forms=ProductForm(request.POST, instance=instance)
        if forms.is_valid():
            forms.save()
            messages.add_message(request, messages.SUCCESS, 'category updated')
            return redirect('/category')
        else:
            messages.add_message(request, messages.ERROR,'failed to update project')
            return render(request,'products/updatecategory.html',{'forms':forms})
        
    context={
        'forms':CategoryForm(instance=instance)
    }
    return render(request, 'products/updatecategory.html',context)

@login_required
@admin_only
def delete_category(request, category_id):
    category=Category.objects.get(id=category_id)
    category.delete()
    messages.add_message(request, messages.SUCCESS, "category deleted")
    return redirect("/products/category")

@login_required
@admin_only
def products(request):
     products=Product.objects.all()
     context={
         'products': products
     }
     return render(request, 'products/products.html',context)