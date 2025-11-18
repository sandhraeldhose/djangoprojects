from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# class based
#function based

# def home(request):
#     return HttpResponse("Welcome to Django")   #message display
#
# def index(request):
#     return HttpResponse("Index page")
#
# def new(request):
#     return HttpResponse("new page")


def home(request):
    context={'Name':'Anu','age':25}
    return render(request,'home.html',context)   # html pade display

def index(request):
    return render(request,'index.html')