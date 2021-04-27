from django.urls import path
from django.urls import path
from .views import ProductView, ProductDetails, cart, checkout, updateItem

urlpatterns = [
    path('', ProductView.as_view(), name='main_page'),
    path('product/<int:pk>', ProductDetails.as_view(), name='details'),
    path('cart', cart, name="cart"),
    path('checkout', checkout, name="checkout"),

    path('update_item/', updateItem, name="update")
]