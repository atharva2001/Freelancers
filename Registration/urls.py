"""Freelancers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from Registration import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('emails', views.emails, name='emails'),
    path('confirm', views.confirm, name='confirm'),
    path('profile', views.profile, name='profile'),
    path('profile/hire', views.hire, name='hire'),
    path('profile/ai', views.ai, name='ai'),
    path('profile/hire/auction', views.auction, name='auction'),
    path('profile/jobs', views.jobs, name='jobs'),
    path('profile/more_details', views.more_details, name='more_details'),
    path('profile/history', views.history, name='history'),
    path('profile/specific_jobs', views.specific_jobs, name='specific_jobs'),
]
