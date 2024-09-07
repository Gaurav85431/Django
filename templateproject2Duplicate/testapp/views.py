from django.shortcuts import render
from django.http import HttpResponse

def template_view(request):
    s= '<html> <body>  <h1> hello welcome to template section  </h1> </body> </html>'

    return HttpResponse(s)

# Create your views here.

