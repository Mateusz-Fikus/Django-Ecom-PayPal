from django.shortcuts import render
from .models import Product
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

class ProductView(ListView):
    model = Product
    context_object_name = 'products'

class ProductDetails(DetailView):
    model = Product
    context_object_name = 'product'

def cart(request):
    return render(request, 'store/cart.html')

def checkout(request):
    return render(request, 'store/checkout.html')