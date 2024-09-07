from django.shortcuts import render
import datetime
# Create your views here.

def wish(request):
    date= datetime.datetime.now()
    h= int(date.strftime('%H'))
   # msg= 'Hello Guest !!! Very Good '
    if h<12:
        return render(request, 'testapp/morning.html', {'d': date})
    elif h<16:
        return render(request, 'testapp/afternoon.html', {'d': date})
    elif h<21:
        return render(request, 'testapp/evening.html', {'d': date})
    else:
        return render(request, 'testapp/night.html', {'d': date})
