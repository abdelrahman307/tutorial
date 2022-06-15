from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request): # a request for a function called index 
    return HttpResponse("index page") # return its response 

def about(request):
    return HttpResponse("about page")