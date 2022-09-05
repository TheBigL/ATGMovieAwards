from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import logout, authenticate, login
from django.conf import settings
from django.shortcuts import redirect


# Create your views here.
def index(response):
    return HttpResponse("Welcome to the ATG Movie Awards!")

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        
        
    else:
        HttpResponse("No User like that exists")
        

def logout(request):

    logout(request)



