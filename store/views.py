from django.shortcuts import render
from .models import Customer, Order, OrderItem, Product, ShippingAddress
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import JsonResponse
import json
from django.http import HttpResponseForbidden
from .utils import cookieCart, cartData, guestOrder

def store(request):

    data = cartData(request)
    cartItems = data['cartItems']

    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems}

    return render(request, 'store/store.html', context)

class ProductDetails(DetailView):
    model = Product
    context_object_name = 'product'

def cart(request):

    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items':items, 'order':order, 'cartItems': cartItems}
    return render(request, 'store/cart.html', context)

def checkout(request):



    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items':items, 'order':order, 'cartItems': cartItems}
    return render(request, 'store/checkout.html', context)


def updateItem(request):

    data = json.loads(request.body)
    productID = data["productID"]
    action = data["action"]
    print(productID, action)

    customer = request.user.customer
    product = Product.objects.get(id=productID)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('item was added', safe=False)

def processOrder(request):

    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        
    else:
        customer, order = guestOrder(request, data)

    total = float(data['form']['total'])

    if total == order.get_cart_total:
        order.complete = True
        order.save()
    
    ShippingAddress.objects.create(
            customer=customer,
            order=order,
            adress=data['shipping']['address'],
            city=data['shipping']['city'],
            vovoideship=data['shipping']['vovoideship'],
            zip_code=data['shipping']['zipcode']
        )

    return JsonResponse('payment complete', safe=False)