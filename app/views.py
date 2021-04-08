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

# Rest Framework API's
class categoryList(APIView):
    def get(self, request):
        categories = Category.objects.all()
        print(categories)
        serialize = CategorySerializer(categories, many=True)
        return Response(serialize.data)
    
class productList(APIView):
    def get(self, request):
        products = []
        category_name = request.GET['category_name']
        result = CatergoryHasProduct.objects.filter(category_name=category_name)
        for r in result:
            products.append(r.product_id)
        serialize = ProductSerializer(products, many=True)
        return Response(serialize.data)

class selectionList(APIView):
    def get(self, request):
        products = []
        product_name = request.GET['product_name']
        product_id = request.GET['product_id']
        with connection.cursor() as cursor:
            cursor.execute("call selectionSubmitted('"+product_id+"')")
            results = dictfetchall(cursor)
        return Response(json.dumps(results))

class productPriceList(APIView):
    def get(self, request):
        product_id = request.GET['product_id']
        temp = []
        with connection.cursor() as cursor:
            cursor.execute("call productPrice('"+product_id+"')")
            results = cursor.fetchall()
        temp = json.dumps(results, cls=DjangoJSONEncoder)
        return Response(temp)

class productManList(APIView):
    def get(self, request):
        product_id = request.GET['product_id']
        with connection.cursor() as cursor:
            cursor.execute("call productManufacturer('"+product_id+"')")
            results = dictfetchall(cursor)
        return Response(json.dumps(results))

class addProductCartList(APIView):    
    def post(self, request, format=None):
        product_id = request.GET['product_id']
        select_product = Product.objects.filter(
            product_id=product_id)
        customer_id = Customer.objects.filter(
            customer_id=1)
        instance = Select.objects.create(customer_id=customer_id[0], 
            product_id=select_product[0])
        serialize = ProductSerializer(select_product, many=True)
        return Response(serialize.data)

class cartPriceList(APIView):
    def get(self, request):
        temp = []
        with connection.cursor() as cursor:
            cursor.execute("call cartPrice()")
            results = cursor.fetchall()
        temp = json.dumps(results, cls=DjangoJSONEncoder)
        return Response(temp)

class cartQuantityList(APIView):
    def get(self, request):
        temp = []
        with connection.cursor() as cursor:
            cursor.execute("call cartQuantity()")
            results = cursor.fetchall()
        temp = json.dumps({'quantity': results})
        return Response(temp)

class removeCartList(APIView):
    def get(self, request):
        product_id = request.GET['product_id']
        select_product = Product.objects.filter(
            product_id=product_id)
        customer_id = Customer.objects.filter(
            customer_id=1)
        instance = Select.objects.filter(customer_id=customer_id[0], 
            product_id=select_product[0])
        instance.delete()
        serialize = ProductSerializer(select_product, many=True)
        return Response(serialize.data)

class cartProductsList(APIView):
    def get(self, request):
        with connection.cursor() as cursor:
            cursor.execute("call cartProducts()")
            results = dictfetchall(cursor)
        return HttpResponse(json.dumps(results))

class productColorsList(APIView):
    def get(self, request):
        product_id = request.GET['product_id']
        with connection.cursor() as cursor:
            cursor.execute("call productColors('"+product_id+"')")
            results = dictfetchall(cursor)
        return HttpResponse(json.dumps(results))

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

# Application API's
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

def selection_submitted(request):
    if request.method == "GET" and request.is_ajax():
        product_id = request.GET.get("product_id", None)
        with connection.cursor() as cursor:
            cursor.execute("call selectionSubmitted('"+product_id+"')")
            results = dictfetchall(cursor)
        return HttpResponse(json.dumps(results), content_type="application/json")
    else:
        return redirect('/')

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

def get_color(request):
    if request.method == "GET" and request.is_ajax():
        product_id = request.GET.get("product_id", None)
        with connection.cursor() as cursor:
            cursor.execute("call productColors('"+product_id+"')")
            results = dictfetchall(cursor)
        return HttpResponse(json.dumps(results), content_type="application/json")
    else:
        return redirect('/')