from django.shortcuts import render, redirect
from .models import *

def store(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/store.html', context)

def cart(request):
    order_id = request.session.get('order', None)
    if order_id is None:
        items = []
        order = {
            'get_cart_total': 0,
            'get_cart_items': 0,
        }
    else:
        order = Order.objects.get(id=order_id)
        items = order.orderitem_set.all()
        order = {
            'get_cart_total': order.get_cart_total,
            'get_cart_items': order.get_cart_items,
        }
        
    context = {
        'items': items,
        'order': order,
    }
    return render(request, 'store/cart.html', context)

def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    order_id = request.session.get('order', None)
    
    if order_id is None:
        order = Order.objects.create(complete=False)
        request.session['order'] = order.id
    else:
        order = Order.objects.get(id=order_id)
        
    order_item, created = OrderItem.objects.get_or_create(order=order, product=product)
    order_item.quantity += 1
    order_item.save()
    
    return redirect('store')

def checkout(request):
    order_id = request.session.get('order', None)
    if order_id is None:
        items = []
        order = {
            'get_cart_total': 0,
            'get_cart_items': 0,
        }
    else:
        order = Order.objects.get(id=order_id)
        items = order.orderitem_set.all()
        order = {
            'get_cart_total': order.get_cart_total,
            'get_cart_items': order.get_cart_items,
        }

    context = {
        'items': items,
        'order': order,
    }
    return render(request, 'store/checkout.html', context)

