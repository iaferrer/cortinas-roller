# -*- coding: utf-8 -*-
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required=True, label="Subject", widget=forms.TextInput(attrs={'class': 'input-text'}))
    email = forms.EmailField(required=True, label="Email", widget=forms.TextInput(attrs={'class': 'input-text'}))
    message = forms.CharField(required=True, max_length=2000, label="Message", widget=forms.Textarea(attrs={'class': 'input-message'}))
