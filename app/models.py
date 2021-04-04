from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Physical_Store(models.Model):
    store_id = models.IntegerField(primary_key=True)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    province =models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    fax_number = models.CharField(max_length=255)
    store_name = models.CharField(max_length=255)

    class Meta:
        ordering = ['store_id']

    def get_store_id(self):
        return self.store_id

    def get_street(self):
        return self.street
    
    def get_city(self):
        return self.city
    
    def get_province(self):
        return self.province

    def get_country(self):
        return self.country

    def get_postal_code(self):
        return self.postal_code
    
    def get_phone(self):
        return self.phone
    
    def get_email(self):
        return self.email

    def get_fax_number(self):
        return self.fax_number

    def get_store_name(self):
        return self.store_name

class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=255)
    product_model = models.CharField(max_length=255)
    product_type = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField()
    product_weight = models.DecimalField(max_digits=5, decimal_places=2)
    store_id = models.ForeignKey(Physical_Store, on_delete=models.CASCADE)

    class Meta:
        ordering = ['product_id']

    def get_product_id(self):
        return self.product_id

    def get_product_name(self):
        return self.product_name
    
    def get_product_model(self):
        return self.product_model
    
    def get_product_type(self):
        return self.product_type

    def get_price(self):
        return self.price

    def get_quantity(self):
        return self.quantity
    
    def get_product_weight(self):
        return self.product_weight
    
    def get_store_id(self):
        return self.store_id

class Order(models.Model):
    order_id = models.IntegerField(primary_key=True)
    order_date = models.DateTimeField() 
    shipped_date = models.DateTimeField() 
    order_status = models.CharField(max_length=255)
    
    def get_order_id(self):
        return self.order_id

    def get_order_date(self):
        return self.order_date
    
    def get_shipped_date(self):
        return self.shipped_date
    
    def get_order_status(self):
        return self.order_status

class Information_Page(models.Model):
    page_id = models.IntegerField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_description = models.CharField(max_length=255)

    def get_page_id(self):
        return self.page_id

    def get_product_id(self):
        return self.product_id
    
    def get_product_description(self):
        return self.product_description

class Manufacturer(models.Model):
    supplier_id = models.IntegerField(primary_key=True)
    supplier_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    fax_number = models.CharField(max_length=255)
    province = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)

    def get_supplier_id(self):
        return self.supplier_id

    def get_supplier_name(self):
        return self.supplier_name
    
    def get_email(self):
        return self.email
    
    def get_city(self):
        return self.city

    def get_country(self):
        return self.country

    def get_phone(self):
        return self.phone

    def get_fax_number(self):
        return self.fax_number

    def get_province(self):
        return self.province
    
    def get_street(self):
        return self.street
  
    def get_postal_code(self):
        return self.postal_code

class Customer(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    fax = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    province = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def get_customer_id(self):
        return self.member_id

    def get_first_name(self):
        return self.first_name
    
    def get_last_name(self):
        return self.last_name

    def get_city(self):
        return self.city
    
    def get_province(self):
        return self.province
    
    def get_postal_code(self):
        return self.postal_code

    def get_email(self):
        return self.email

    def get_phone(self):
        return self.phone

    def get_fax(self):
        return self.fax

    def get_street(self):
        return self.street

    def get_country(self):
        return self.country

class Inventory_Website(models.Model):
    business_licence = models.IntegerField(primary_key=True)
    web_address = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    def get_business_licence(self):
        return self.business_licence

    def get_web_address(self):
        return self.web_address
    
    def get_name(self):
        return self.name

class Web_Admin(models.Model):
    admin_id = models.IntegerField(primary_key=True)
    admin_fname = models.CharField(max_length=255)
    admin_lname = models.CharField(max_length=255)
    admin_password = models.CharField(max_length=255)
    salary = models.IntegerField()
    business_licence = models.ForeignKey(Inventory_Website, on_delete=models.CASCADE)

    def get_admin_id(self):
        return self.admin_id

    def get_admin_fname(self):
        return self.admin_fname
    
    def get_admin_lname(self):
        return self.admin_lname
    
    def get_admin_password(self):
        return self.admin_password

    def get_salary(self):
        return self.salary

    def get_business_licence(self):
        return self.business_licence

class Manager(models.Model):
    manager_id = models.IntegerField(primary_key=True)
    man_fname = models.CharField(max_length=255)
    man_lname = models.CharField(max_length=255)
    man_salary = models.CharField(max_length=255)

    def get_manager_id(self):
        return self.manager_id

    def get_man_fname(self):
        return self.man_fname
    
    def get_man_lname(self):
        return self.man_lname
    
    def get_man_salary(self):
        return self.man_salary

class Request(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)

    def get_customer_id(self):
        return self.customer_id

    def get_order_id(self):
        return self.order_id

class Shipper(models.Model):
    shipper_id = models.IntegerField(primary_key=True)
    shipper_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    fax_number = models.CharField(max_length=255)

    def get_shipper_id(self):
        return self.shipper_id

    def get_shipper_name(self):
        return self.shipper_name
    
    def get_phone(self):
        return self.phone
    
    def get_email(self):
        return self.email

    def get_fax_number(self):
        return self.fax_number

class ShippedBy(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    shipper_id = models.ForeignKey(Shipper, on_delete=models.CASCADE)

    def get_order_id(self):
        return self.order_id

    def get_shipper_id(self):
        return self.shipper_id

class Colour(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    colour = models.CharField(max_length=255)

    def get_product_id(self):
        return self.product_id

    def get_colour(self):
        return self.colour

class Supply(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    supplier_id = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

    def get_product_id(self):
        return self.product_id

    def get_supplier_id(self):
        return self.supplier_id

class Category(models.Model):
    category_name = models.CharField(max_length=255, primary_key=True)
    category_description = models.CharField(max_length=255)

    def get_category_name(self):
        return self.category_name

    def get_category_description(self):
        return self.category_description

class CatergoryHasProduct(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE)

    def get_product_id(self):
        return self.product_id

    def get_category_name(self):
        return self.category_name  

class Customer_Support(models.Model):
    cust_sup_id = models.IntegerField(primary_key=True)
    cust_sup_fname = models.CharField(max_length=255)
    cust_sup_lname = models.CharField(max_length=255)
    business_licence = models.ForeignKey(Inventory_Website, on_delete=models.CASCADE)

    def cust_sup_id(self):
        return self.cust_sup_id

    def get_cust_sup_fname(self):
        return self.cust_sup_fname
    
    def get_cust_sup_lname(self):
        return self.cust_sup_lname
    
    def get_business_licence(self):
        return self.business_licence

class Cart(models.Model):
    number_of_products = models.IntegerField()
    total_price = models.DecimalField(max_digits=6, decimal_places=2)

    def get_number_of_products(self):
        return self.number_of_products

    def get_total_price(self):
        return self.total_price

class Assist(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    cust_sup_id = models.ForeignKey(Customer_Support, on_delete=models.CASCADE)
    call = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    live_chat = models.CharField(max_length=255)

    def cust_sup_id(self):
        return self.cust_sup_id

    def get_customer_id(self):
        return self.customer_id

class Select(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

    def get_customer_id(self):
        return self.customer_id

    def get_product_id(self):
        return self.product_id

class ProductFoundStore(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    store_id = models.ForeignKey(Physical_Store, on_delete=models.CASCADE)

    def get_product_id(self):
        return self.product_id

    def get_store_id(self):
        return self.store_id