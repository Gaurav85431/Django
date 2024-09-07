from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def template_view(request):
    s='<html><body><h1> Hello Welcome to template section </h1></body></html>'
    return HttpResponse(s)
