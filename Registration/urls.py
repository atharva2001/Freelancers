from django.contrib import admin
from django.urls import path
from Registration import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='index'),
    path('login/login', views.login, name='login'),
]
