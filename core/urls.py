# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this
from django.conf.urls import url
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    url(r'users/', views.userList.as_view()),
    url(r'groups/', views.groupList.as_view()),
    url(r'stores/', views.storeList.as_view()),
    url(r'products/', views.productList.as_view()),
    path("", include("authentication.urls")), # Auth routes - login / register
    path("", include("app.urls")),             # UI Kits Html files
]
