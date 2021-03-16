# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin

# Register your models here.
from .models import Product, Physical_Store

admin.site.register(Product)
admin.site.register(Physical_Store)