"""Nameste URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index.as_view(), name="Index"),
    path('shop/', views.shop.as_view(), name="Shop"),
    path('cart/', views.cart.as_view(), name="Cart"),
    path('checkout/', views.checkout.as_view(), name='Checkout'),
    path('update_item/', views.updateItem.as_view(), name='updateitem'),
    path('process_order/', views.processOrder.as_view(), name='processorder')
]
