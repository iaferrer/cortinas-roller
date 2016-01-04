# -*- coding: utf-8 -*-
# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from mainApp.models import *
from django.template.loader import render_to_string
from django.utils import timezone
import json

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def catalogue(request):
    data = {}
    data['product_types'] = Type.objects.order_by('name')
    return render(request, 'catalogue.html', data)

def quote(request):
    return render(request, 'quote.html')

def contact(request):
    return render(request, 'contact.html')

def load_products(request, type):
    response = {'ok': False}
    cap_type = type.lower().capitalize()
    ans = Product.objects.filter(product_type=cap_type)
    if ans:
        response['first_html'] = render_to_string('_product.html', {'product': ans[0]})
        response['rest_html'] = render_to_string('_products.html', {'products': ans[1:]})
        response['ok'] = True
    return HttpResponse(json.dumps(response))
