# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.utils.html import mark_safe

class Type(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    photo = models.FileField(upload_to='photos/')
    active = models.BooleanField(default=True)
    def __str__(self):
        return mark_safe(self.name.upper())
    def photo_url(self):
        return '/media/' + "/".join(str(self.photo).split('/')[-2:])

class Product(models.Model):
    product_type = models.ForeignKey(Type)
    name = models.CharField(max_length=100, primary_key=True)
    photo = models.FileField(upload_to='photos/')
    def __str__(self):
        return mark_safe(self.name)
    def photo_url(self):
        return '/media/' + "/".join(str(self.photo).split('/')[-2:])
