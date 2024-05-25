from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from watchapp.models import Product
from .models import Cart

@login_required(login_url='auth:login')  # Ensure user is logged in to access this view
def addcart(request, id):
    user = request.user
    product = Product.objects.get(id=id)
    try:
        cart = Cart.objects.get(product=product, user=user)
        if cart.quantity < cart.product.stock:
            cart.quantity += 1
            cart.save()
    except Cart.DoesNotExist:
        Cart.objects.create(user=user, product=product, quantity=1)
    return redirect('cartapp:displaycart')
    
def displaycart(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    total = sum(cart_item.product.price * cart_item.quantity for cart_item in cart) -20
    return render(request, 'cart.html', {'cart': cart, 'total': total})

def removecart(request, id):
    user = request.user
    product = Product.objects.get(id=id)
    cart = Cart.objects.get(product=product, user=user)
    if cart.quantity > 1:
        cart.quantity -= 1
        cart.save()
    return redirect('cartapp:displaycart')

def fullremove(request, id):
    user = request.user
    product = Product.objects.get(id=id)
    cart = Cart.objects.get(product=product, user=user)
    cart.delete()
    return redirect('cartapp:displaycart')     

def placeorder(request):
    user = request.user
    carts = Cart.objects.filter(user=user)
    for cart in carts:
        prod = Product.objects.get(id=cart.product.id)
        prod.stock -= cart.quantity
        prod.save()
        cart.delete()
    return redirect('shop:home')
