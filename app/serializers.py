from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User, Group

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Physical_Store
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class InformationPage(serializers.ModelSerializer):
    class Meta:
        model = Information_Page
        fields = '__all__'

class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class WebsiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory_Website
        fields = '__all__'

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Web_Admin
        fields = '__all__'

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = '__all__'

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'

class ShipperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipper
        fields = '__all__'

class ShippedBySerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippedBy
        fields = '__all__'

class ColourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colour
        fields = '__all__'

class SupplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Supply
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CatergoryHasProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatergoryHasProduct
        fields = '__all__'

class CustomerSupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer_Support
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class AssistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assist
        fields = '__all__'

class SelectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Select
        fields = '__all__'