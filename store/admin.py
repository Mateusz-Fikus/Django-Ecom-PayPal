from django.contrib import admin
from .models import Customer, Order, OrderItem, Product, ShippingAddress

admin.site.register(Customer)
admin.site.register(Product)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["customer", "date_ordered", "transaction_id"]


admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
