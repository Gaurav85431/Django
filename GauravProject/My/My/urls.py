"""My URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from My import views  #My se view.py ko import karo apne project me taaki ,, My folder se views ko import karna hai



urlpatterns = [
    path('admin_gaurav/', admin.site.urls),
    path('aboutus/', views.aboutus),  # aboutus url per function call hoga  I.E. VIEWS SE ABOUTUS KO CALL KARNA HAI
    path('', views.homePage),
    path('hPage', views.hPage),
    path('home/', views.home),
    path('last/', views.last),
    path('gaurav/', views.gaurav),
    path('Page/', views.Page),
    path('MyPage/', views.MyPage),
    path('choose/', views.choose),
    path('web/', views.web ),

   # path('course/<slug:courseid>',views.courseDetails),
   #yadi kisi type ka value aa sakta hai to ::::::
   path('course/<courseid>',views.courseDetails),
]

'''
 path('course/<int:courseid>',views.courseDetails),
    path('course/<str:courseid>',views.courseDetails),
   
'''