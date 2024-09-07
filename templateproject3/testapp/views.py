from django.shortcuts import render
import datetime



def template_view(request):
    dt= datetime.datetime.now()
    my_dict= {'date': dt}
#    return render(request, 'results.html')
    #return(s)
    return render(request, 'results.html', context=my_dict)

