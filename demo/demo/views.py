from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
  data={
'title': 'Home New',
'bdata':'welcome to django',
'clist':['php','java', 'django' ],
'numbers': [10, 20, 30, 40, 50],
'num': [],
'student_details':[
    {'name':'pradeep', 'phone':9269698122},
    {'name':'sumit', 'phone':9269698123}

]

  }
  return render(request,"index1.html", data)

def home(request):
  return render(request,"index.html")

def aboutUs(request):
  return HttpResponse("welcome to the django")

def course(request):
  return HttpResponse("welcome to the course of django")

def CourseDetails(request, courseid):
  return HttpResponse(courseid)
