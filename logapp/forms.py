# -*- coding: utf-8 -*-
from django import forms

class Authform (forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput({'class': 'form-control'}), label='Имя')
    password = forms.CharField(widget=forms.PasswordInput({'class': 'form-control'}), label='Пароль')