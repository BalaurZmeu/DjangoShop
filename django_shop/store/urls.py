from django.urls import path
from .views import *

urlpatterns = [
    path('', store, name="store"),
    path('cart/', cart, name="cart"),
    path('checkout/', checkout, name="checkout"),
    path('add_to_cart/<int:product_id>/', add_to_cart, name="add_to_cart"),
]

