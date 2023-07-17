"""personaltraining URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.shortcuts import render
from django.urls import path, include


def home(request):
    return render(request, 'home.html')  # bad practice remove and fix asap


def login(request):
    return render(request, 'login.html')  # bad practice remove and fix asap


urlpatterns = [
    path('', login),
    path('', home),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
]
