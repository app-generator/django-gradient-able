# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Physical_Store(models.Model):
    store_id = models.IntegerField(primary_key=True)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    province =models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    postal_code =models.CharField(max_length=255)
    phone = models.IntegerField()
    email = models.EmailField()
    fax_number = models.IntegerField()

class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=255)
    product_model = models.CharField(max_length=255)
    product_type = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField()
    product_weight = models.DecimalField(max_digits=5, decimal_places=2)
    store_id = models.ForeignKey(Physical_Store, on_delete=models.CASCADE)

class Order(models.Model):
    order_id = models.IntegerField(primary_key=True)
    order_date = models.DateTimeField() 
    shipped_date = models.DateTimeField() 
    order_status = models.CharField(max_length=255)

class Information_Page(models.Model):
    page_id = models.IntegerField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_description = models.CharField(max_length=255)

class Manufacturer(models.Model):
    supplier_id = models.IntegerField(primary_key=True)
    supplier_name = models.CharField(max_length=255)
    email = models.EmailField()
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    phone = models.IntegerField()
    fax_number = models.IntegerField()
    province = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)

class Member(models.Model):
    member_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    shipping_address = models.CharField(max_length=255)
    billing_address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    province = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    email_address = models.EmailField()

class Inventory_Website(models.Model):
    business_licence = models.IntegerField(primary_key=True)
    web_address = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

class Web_Admin(models.Model):
    admin_id = models.IntegerField(primary_key=True)
    admin_fname = models.CharField(max_length=255)
    admin_lname = models.CharField(max_length=255)
    admin_password = models.CharField(max_length=255)
    salary = models.IntegerField()
    business_licence = models.ForeignKey(Inventory_Website, on_delete=models.CASCADE)

class Individual_User(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    business_licence = models.ForeignKey(Inventory_Website, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=255)
    customer_contact = models.CharField(max_length=255)

class Request(models.Model):
    customer_id = models.ForeignKey(Individual_User, on_delete=models.CASCADE)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)

class Shipper(models.Model):
    shipper_id = models.IntegerField(primary_key=True)
    shipper_name = models.CharField(max_length=255)
    phone = models.IntegerField()
    email = models.EmailField()
    fax_number = models.IntegerField()

class ShippedBy(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    shipper_id = models.ForeignKey(Shipper, on_delete=models.CASCADE)

class Colour(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    colour = models.CharField(max_length=255)

class Supply(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    supplier_id = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

class Category(models.Model):
    category_name = models.CharField(max_length=255, primary_key=True)
    category_description = models.CharField(max_length=255)

class Has(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE)

class Customer_Support(models.Model):
    cust_sup_id = models.IntegerField(primary_key=True)
    cust_sup_fname = models.CharField(max_length=255)
    cust_sup_lname = models.CharField(max_length=255)
    business_licence = models.ForeignKey(Inventory_Website, on_delete=models.CASCADE)

class Cart(models.Model):
    number_of_products = models.IntegerField()
    total_price = models.DecimalField(max_digits=6, decimal_places=2)

class Assist(models.Model):
    customer_id = models.ForeignKey(Individual_User, on_delete=models.CASCADE)
    cust_sup_id = models.ForeignKey(Customer_Support, on_delete=models.CASCADE)

class Select(models.Model):
    customer_id = models.ForeignKey(Individual_User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)