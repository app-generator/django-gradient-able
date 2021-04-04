"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse, JsonResponse
from django import template
from rest_framework import viewsets, permissions
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from .serializers import *
from .models import *
from django.contrib.auth.models import User, Group
from django.db import connection
import pdb
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.db import connections

# class userList(APIView):
#     def get(self, request):
#         users = User.objects.all()
#         serialize = UserSerializer(users, many=True)
#         return Response(serialize.data)  
#     def post(self, request, format=None):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class groupList(APIView):
#     def get(self, request):
#         groups = Group.objects.all()
#         serialize = GroupSerializer(groups, many=True)
#         return Response(serialize.data)
#     def post(self, request, format=None):
#         serializer = GroupSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class storeList(APIView):
    def get(self, request):
        stores = Physical_Store.objects.all()
        serialize = StoreSerializer(stores, many=True)
        return Response(serialize.data)
    
    def post(self, request, format=None):
        serializer = StoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class productList(APIView):
    def get(self, request):
        products = Product.objects.raw('SELECT * FROM app_product')
        serialize = ProductSerializer(products, many=True)
        return Response(serialize.data)
    
    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class productDetail(APIView):
    """
    Retrieve, update or delete a product instance.
    """
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class productList(APIView):
#     def get(self, request):
#         products = Product.objects.all()
#         serialize = ProductSerializer(products, many=True)
#         return Response(serialize.data)  
#     def post(self, request, format=None):
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@login_required(login_url="/login/")
def index(request):
    
    context = {}
    context['segment'] = 'index'

    html_template = loader.get_template( 'index.html' )
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template      = request.path.split('/')[-1]
        context['segment'] = load_template
        
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))

def dictfetchall(cursor): 
    "Returns all rows from a cursor as a dict" 
    desc = cursor.description 
    return [
            dict(zip([col[0] for col in desc], row)) 
            for row in cursor.fetchall() 
    ]

def get_category(request):
    if request.method == "GET" and request.is_ajax():
        result_set = []
        with connection.cursor() as cursor:
            cursor.execute("call getCategory()")
            results = dictfetchall(cursor)

        return HttpResponse(json.dumps(results), content_type="application/json")
    else:
        return redirect('/')

# def get_products(request):
#     if request.method == "GET" and request.is_ajax():
#         # get name of user selected building
#         category_name = request.GET.get("category", None)
#         result_set = []
#         all_products = []
#         temp = []
#         selected_category = CatergoryHasProduct.objects.filter(
#             category_name=category_name)  # get field object that matches the selected category     
#         for cat in selected_category:
#             temp.append(cat.product_id.product_id)
#         all_products = Product.objects.filter(product_id__in=temp)
#         for product in all_products:  
#             result_set.append(
#                 {'product_id': product.product_id, 'product_name': product.product_name}) 
#         return HttpResponse(json.dumps(result_set), content_type="application/json")
#     else:
#         return redirect('/')

def get_products(request):
    if request.method == "GET" and request.is_ajax():
        result_set = []
        category_name = request.GET.get("category", None)
        with connection.cursor() as cursor:
            cursor.execute("call getProducts('"+category_name+"')")
            results = dictfetchall(cursor)
        for product in results:
            result_set.append(
                {'product_id': product['product_id'], 'product_name': product['product_name']}) 
        return HttpResponse(json.dumps(result_set), content_type="application/json")
    else:
        return redirect('/')

# def selection_submitted(request):
#     if request.method == "GET" and request.is_ajax():
#         product_id = request.GET.get("product_id", None)
#         selected_product = Product.objects.get(
#             product_id=product_id)
#         selected_store = Physical_Store.objects.get(
#              store_id=selected_product.store_id.store_id)
#         info_page = Information_Page.objects.get(
#             product_id = product_id)   
#         temp = json.dumps(selected_product.price, cls=DjangoJSONEncoder)
#         return HttpResponse(json.dumps({'product_name': selected_product.product_name,
#                                         'store_name': selected_store.store_name,
#                                         'product_description': info_page.product_description}),
#                             content_type="application/json")
#     else:
#         return redirect('/')

def selection_submitted(request):
    if request.method == "GET" and request.is_ajax():
        product_id = request.GET.get("product_id", None)
        with connection.cursor() as cursor:
            cursor.execute("call selectionSubmitted('"+product_id+"')")
            results = dictfetchall(cursor)
        return HttpResponse(json.dumps(results), content_type="application/json")

    else:
        return redirect('/')

# def product_price(request):
#     if request.method == "GET" and request.is_ajax():
#         product_id = request.GET.get("product_id", None)
        # selected_product = Product.objects.get(
        #     product_id=product_id)
#         temp = []  
#         temp = json.dumps(selected_product.price, cls=DjangoJSONEncoder)
#         return HttpResponse(temp, content_type="application/json")
#     else:
#         return redirect('/')

def product_price(request):
    if request.method == "GET" and request.is_ajax():
        product_id = request.GET.get("product_id", None)
        temp = []
        with connection.cursor() as cursor:
            cursor.execute("call productPrice('"+product_id+"')")
            results = cursor.fetchall()
        temp = json.dumps(results, cls=DjangoJSONEncoder)
        return HttpResponse(temp, content_type="application/json")
    else:
        return redirect('/')

# def product_manufacturer(request):
#     if request.method == "GET" and request.is_ajax():
#         product_id = request.GET.get("product_id", None)
#         selected_product = Supply.objects.filter(
#             product_id=product_id)
#         temp = []
#         result_set = []
#         for prod in selected_product:
#             temp.append(prod.supplier_id.supplier_id)
#         all_suppliers = Manufacturer.objects.filter(supplier_id__in=temp)
#         for supplier in all_suppliers:  
#             result_set.append(
#                 {'supplier_id': supplier.supplier_id, 'supplier_name': supplier.supplier_name})
#         return HttpResponse(json.dumps(result_set),
#                             content_type="application/json")
#     else:
#         return redirect('/')

def product_manufacturer(request):
    if request.method == "GET" and request.is_ajax():
        product_id = request.GET.get("product_id", None)
        with connection.cursor() as cursor:
            cursor.execute("call productManufacturer('"+product_id+"')")
            results = dictfetchall(cursor)
        return HttpResponse(json.dumps(results),
                            content_type="application/json")
    else:
        return redirect('/')

@csrf_exempt
def add_product_cart(request):
    if request.method == "POST" and request.is_ajax():
        product_id = request.POST.get("product_id", None)
        select_product = Product.objects.filter(
            product_id=product_id)
        customer_id = Customer.objects.filter(
            customer_id=1)
        instance = Select.objects.create(customer_id=customer_id[0], 
            product_id=select_product[0])
        return redirect('/')

def cart_price(request):
    if request.method == "GET" and request.is_ajax():
        temp = []
        with connection.cursor() as cursor:
            cursor.execute("call cartPrice()")
            results = cursor.fetchall()
        temp = json.dumps(results, cls=DjangoJSONEncoder)
        return HttpResponse(temp, content_type="application/json")
    else:
        return redirect('/')

def cart_quantity(request):
    if request.method == "GET" and request.is_ajax():
        temp = []
        with connection.cursor() as cursor:
            cursor.execute("call cartQuantity()")
            results = cursor.fetchall()
        temp = json.dumps({'quantity': results})
        return HttpResponse(temp, content_type="application/json")
    else:
        return redirect('/')

def remove_cart(request):
    if request.method == "GET" and request.is_ajax():
        product_id = request.GET.get("product_id", None)
        select_product = Product.objects.filter(
            product_id=product_id)
        customer_id = Customer.objects.filter(
            customer_id=1)
        instance = Select.objects.filter(customer_id=customer_id[0], 
            product_id=select_product[0])
        instance.delete()
        return redirect('/')

def cart_products(request):
    if request.method == "GET" and request.is_ajax():
        with connection.cursor() as cursor:
            cursor.execute("call cartProducts()")
            results = dictfetchall(cursor)
        return HttpResponse(json.dumps(results), content_type="application/json")
    else:
        return redirect('/')