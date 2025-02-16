from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

def HomePage(request):
    return render(request, 'index.html')
