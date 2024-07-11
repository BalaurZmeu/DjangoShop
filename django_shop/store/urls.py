from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name="store"),
    path('register/', views.register, name='register'),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('product/<int:pk>', views.product, name='product'),

    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
]
