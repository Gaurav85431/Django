from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def time_info(request):
    time= datetime.datetime.now()
    s='<h1> Hello current Date and Time is : '+str(time)+' </h1>'
    return HttpResponse(s)