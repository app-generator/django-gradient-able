# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this
from django.conf.urls import url
from app import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    # url(r'users/', views.userList.as_view()),
    # url(r'groups/', views.groupList.as_view()),
    path('stores/', views.storeList.as_view()),
    path('products/', views.productList.as_view()),
    path('products/<int:pk>/', views.productDetail.as_view()),
    path('get_category/', views.get_category, name='get-category'),
    path('get_products/', views.get_products, name='get-products'),
    path('selection_submitted/', views.selection_submitted, name='selection-submitted'),
    path('product_price/', views.product_price, name='product-price'),
    path('product_manufacturer/', views.product_manufacturer, name='product-manufacturer'),     
    path('add_product_cart/', views.add_product_cart, name='add-cart'),     
    path('cart_price/', views.cart_price, name='cart-price'),     
    path('cart_quantity/', views.cart_quantity, name='cart-quantity'),     
    path('remove_cart/', views.remove_cart, name='remove-cart'),     
    path('cart_products/', views.cart_products, name='cart-products'),     
    path("", include("authentication.urls")), # Auth routes - login / register
    path("", include("app.urls")),             # UI Kits Html files
]
urlpatterns = format_suffix_patterns(urlpatterns)