from django.shortcuts import render
import datetime
# Create your views here.
def template_view(request):
    dt= datetime.datetime.now()
    my_dict= {'date': dt}
    return render(request, 'testapp/results.html', context=my_dict)
