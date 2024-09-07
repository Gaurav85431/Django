from django.shortcuts import render

# Create your views here.
import datetime
from django.http import HttpResponse
def date_time(request):
    date= datetime.datetime.now()
    s='<h1> The current date and time at server is :'+str(date)+' </h1>'
    return HttpResponse(s)