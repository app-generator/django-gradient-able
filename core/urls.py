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
    # Rest framework api's
    path('get_category_api/', views.categoryList.as_view()),
    url(r'^get_products_api/$', views.productList.as_view()),
    url(r'^selection_submitted_api/$', views.selectionList.as_view()),
    url(r'^product_price_api/$', views.productPriceList.as_view()),
    url(r'^product_manufacturer_api/$', views.productManList.as_view()),     
    url(r'add_product_cart_api/$', views.addProductCartList.as_view()),     
    path('cart_price_api/', views.cartPriceList.as_view()),     
    path('cart_quantity_api/', views.cartQuantityList.as_view()),     
    url(r'remove_cart_api/$', views.removeCartList.as_view()),     
    url(r'cart_products_api/$', views.cartProductsList.as_view()),
    url(r'get_color_api/$', views.productColorsList.as_view()),
    url(r'update_product_quantity_api/$', views.productQuantityUpdateList.as_view()),
    # App ajax api's
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
    path('get_color/', views.get_color, name='get-color'),      
    path('update_product_quantity/', views.update_product_quantity, name='update-product-quantity'),              
    path("", include("authentication.urls")), # Auth routes - login / register
    path("", include("app.urls")),             # UI Kits Html files
]
urlpatterns = format_suffix_patterns(urlpatterns)