from django.contrib import admin
from django.urls import path
from newApp import views

urlpatterns = [
    path('',views.index,name="home"),
    path('index',views.index,name="index"),
    path('about',views.about,name="about"),
    path('service',views.service,name="service"),
    path('blog',views.blog,name="Blog")
]
