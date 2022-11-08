from django.contrib import admin
from django.urls import path
from Registration import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('profile', views.profile, name='profile'),
    path('emails', views.emails, name='emails'),
    path('confirm', views.confirm, name='confirm'),
]
