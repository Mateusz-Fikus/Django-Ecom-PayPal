from django.contrib import admin
from .models import Customer, Order, OrderItem, Product, ShippingAddress

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
