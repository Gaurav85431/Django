from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def test(request):
    return HttpResponse('<h1> Hello friends Good Morning ... Have a nice Day </h1>')