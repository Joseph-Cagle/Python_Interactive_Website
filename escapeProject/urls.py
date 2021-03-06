"""escapeProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from escapeApp import views 

#from django.urls import path, include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.homePage, name='home'),
    #redirect root to page we want to create
    url(r'^adventure/$', views.adventurePage, name='adventure'),
    url(r'^character.html$', views.character_page, name='character'),
    url(r'^character/$', views.character_page, name='character'),
    url(r'^character/home.html$', views.homePage, name='home'),
    url(r'^adventure/home.html$', views.homePage, name='home'),
    url(r'^adventureRight/$', views.adventureRight, name='Right'),
    url(r'^adventureRight/home.html$', views.homePage, name='home'),
    url(r'^adventureLeft/$', views.adventureLeft, name='Left'),
    url(r'^adventureLeft/home.html$', views.homePage, name='home'),
     url(r'^adventureStraight/$', views.adventureStraight, name='straight'),
    url(r'^adventureStraight/home.html$', views.homePage, name='home'),
    url(r'^backAtVault/$', views.backToVault, name='back'),
    url(r'^backAtVault/home.html$', views.homePage, name='home'),
    url(r'^backAtVault/straight.html$', views.adventureStraight, name='straight'),
    #url('',include("django.contrib.auth.urls")),
    #url("register/", views.register, name ='register')
    url(r'^register', views.register, name='register'),
    
   
]
