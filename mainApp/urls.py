from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^about/', views.about, name='about'),
    url(r'^catalogue/', views.catalogue, name='catalogue'),
    url(r'^quote/', views.quote, name='quote'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^products/(?P<type>\w+)/', views.load_products, name='products'),
    url('', views.index, name='index'),
]
