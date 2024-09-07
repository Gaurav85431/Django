from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def Good_Morning(request):
    return HttpResponse('<h1>Hello friends good morning</h1>')
def Good_Evening(request):
    return HttpResponse('<h1>Hello friends good evening</h1>')
def Good_Afternoon(request):
    return HttpResponse('<h1>Hello friends good afternoon</h1>')
