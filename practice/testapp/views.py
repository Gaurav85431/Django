from django.shortcuts import render
from django.http import HttpResponse
import datetime

def Home(request):
    dt = datetime.datetime.now()
  
    return render(request, "index.html", {'date' :dt})

