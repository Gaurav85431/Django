from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    return render(request, "index4.html")

def hPage(request):
    return render(request, "indx5.html")

def Page(request):
    p = {'title' : "GP"}
    return render(request, "g.html", p)

def web(request):
    dt = {
          'body' : 'Good Morning',
          'title' : 'Hello',
          'clist' : ['html','Java','php','Django']
          
          }
    return render(request, "g1.html",dt)

def choose(request):
    dt = {
          'body' : 'Good Morning',
          'title' : 'Hello',
          'clist' : ['html','Java','php','Django'],
          
           'num': [10,20,30,40,50],
        


            'x' : [15,5,8,7,6,5,12],
          'student_details': [
           
           {'name':'Pradeep', 'Phone': 9006006045},
           {'name':'testing', 'Phone': 8841654114}
          
             ]   
        

        

    }
    return render(request, "g2.html",dt)

def MyPage(request):
    data={
          'title' : 'My Page'

    }
    return render(request, "abc.html",data)



def aboutus(request):
    return HttpResponse("welcome to django by gaurav")
def home(request):
    return HttpResponse("<h1> welcome to home of django </h2>")
def last(request):
    return HttpResponse("welcome to last ")

def gaurav(request):
    return HttpResponse("welcome  gaurav  in django")

def courseDetails(request, courseid):
    return HttpResponse(courseid)