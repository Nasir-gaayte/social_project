from curses.ascii import CR
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import forms
# Create your views here.


class SingUp(CreateView):
    form_class = forms.User_createForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/singup.html'
