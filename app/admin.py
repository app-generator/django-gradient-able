# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin

# Register your models here.
from .models import Product, Physical_Store, Category, CatergoryHasProduct, Colour, Customer, Information_Page, Manufacturer, Supply, Order

admin.site.register(Product)
admin.site.register(Physical_Store)
admin.site.register(Category)
admin.site.register(CatergoryHasProduct)
admin.site.register(Colour)
admin.site.register(Customer)
admin.site.register(Information_Page)
admin.site.register(Manufacturer)
admin.site.register(Supply)
admin.site.register(Order)