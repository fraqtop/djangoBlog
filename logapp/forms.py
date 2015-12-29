# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm

class Authform (forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput({'class': 'form-control'}), label='Имя')
    password = forms.CharField(widget=forms.PasswordInput({'class': 'form-control'}), label='Пароль')


class Regform (UserCreationForm):
    username = forms.CharField(max_length=50, widget=forms.TextInput({'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput({'class': 'form-control'}), label='Пароль')
    password2 = forms.CharField(widget=forms.PasswordInput({'class': 'form-control'}), label='Повторите пароль')