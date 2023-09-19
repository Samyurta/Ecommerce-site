from django.shortcuts import render, redirect
from products.models import *
from django.contrib.auth.decorators import login_required
from.models import Cart
from django.contrib import messages

# Create your views here.
def index(request):
    products=Product.objects.all().order_by('-id')[:8]
    context={
        'products':products
    }
    return render(request, 'users/index.html',context)

def products(request):
    products=Product.objects.all()
    context={
        'products':products
    }
    return render(request, 'users/products.html',context)

def productdetails(request, product_id):
    product=Product.objects.get(id=product_id)
    context={
        'product':product
    }
    return render(request, 'users/productdetails.html', context)
@login_required
def add_to_cart(request, product_id):
    user=request.user
    product=Product.objects.get(id=product_id)
    check_items_presence=Cart.objects.filter(user=user,product=product)
    if check_items_presence:
        messages.add_message(request,messages.ERROR,'product is already present in the cart')
        return redirect('/productlist')
    else:
        cart=Cart.objects.create(product=product,user=user)
        if cart:
            messages.add_message(request,messages.SUCCESS,'product added to cart')
            return redirect('/mycart')
        else:
            messages.add_message(request,messages.ERROR,'something went wrong')
@login_required
def show_cart_items(request):
    user=request.user
    items=Cart.objects.filter(user=user)
    context={
        'items':items
    }
    return render(request, 'users/cart.html', context)
@login_required
def remove_cart_items(request,cart_id):
    items=Cart.objects.get(id=cart_id)
    items.delete()
    messages.add_message(request, messages.SUCCESS, 'item removed from the cart')
    return redirect('/cart')