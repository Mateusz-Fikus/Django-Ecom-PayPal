
from django.shortcuts import render
from .models import Order, Product
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import JsonResponse
import json


class ProductView(ListView):
    model = Product
    context_object_name = 'products'

class ProductDetails(DetailView):
    model = Product
    context_object_name = 'product'

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}

    context = {'items':items, 'order':order}
    return render(request, 'store/cart.html', context)

def checkout(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}

    context = {'items':items, 'order':order}
    return render(request, 'store/checkout.html', context)


def updateItem(request):

    data = json.load(request.data)
    


    return JsonResponse('item was added', safe=False)