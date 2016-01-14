# -*- coding: utf-8 -*-
# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from mainApp.models import *
from mainApp.forms import ContactForm
from django.template.loader import render_to_string
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
import json
import requests

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
    data = {'form': ContactForm()}
    return render(request, 'contact.html', data)

def load_products(request, type):
    response = {'ok': False}
    cap_type = type.lower().capitalize().replace ("_", " ")
    ans = Product.objects.filter(product_type=cap_type)
    if ans:
        response['first_html'] = render_to_string('_product.html', {'product': ans[0]})
        response['rest_html'] = render_to_string('_products.html', {'products': ans[1:]})
        response['ok'] = True
    return HttpResponse(json.dumps(response))

@csrf_exempt
def send_message(request):

    name = request.POST.get('name')
    email = request.POST.get('email')
    tmp_message = request.POST.get('message')

    subject = '[RollerCo Contact] ' + name.capitalize();
    message = 'From: ' + name + ' <' + email + '>\n\n' + tmp_message

    response = {'ok': True}
    a = requests.post(
            "https://api.mailgun.net/v3/rollerco.cl/messages",
            auth = ("api", "key-466488578d0fb8c68531bfd504831629"),
            data = {
                "from": "Contact Manager <contact@rollerco.cl>",
                "to": "ignacio.ferrer92@gmail.com",
                "subject": subject,
                "text": message
                }
        )
    print(a);
    return HttpResponse(json.dumps(response))
