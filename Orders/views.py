from django.template import context 
from django.shortcuts import render
from django.contrib.auth import login, logout

from rest_framework.generics import ListAPIView,CreateAPIView
def details(request):   

    return render(request,"index.html")

def Auth(request):
    return render(request,"Authorization.html")