from django.shortcuts import render
from django.views.generic import CreateView
from django.http import HttpResponseRedirect
from .models import Contact


def addContact(request):
    email=request.GET.get('emails')
    mail= Contact.objects.create(email=email)
    return HttpResponseRedirect('/')