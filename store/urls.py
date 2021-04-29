from django.urls import path
from django.urls import path
from .views import store, ProductDetails, cart, checkout, updateItem, processOrder

urlpatterns = [
    path('', store, name='main_page'),
    path('product/<int:pk>', ProductDetails.as_view(), name='details'),
    path('cart', cart, name="cart"),
    path('checkout', checkout, name="checkout"),

    path('update_item/', updateItem, name="update"),
    path('process_order/', processOrder, name="process_order")
]