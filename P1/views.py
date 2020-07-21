from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return HttpResponse("hello world")

def home(request):
    return HttpResponse("<h1>welcome to homepage</h1>")

def html_demo1(request):
    return render(request,"sample.html")

def html_demo2(request):
    return render(request,"sample2.html")

def third(request):
    return render(request,"third.html",context={'data':"akshay",'name':"kishan"})

def fourth(request):
    fruits=['apple','mango','banana','kiwi','orange']
    return render(request,"fourth.html",context={'fruits':fruits})

def fifth(request):
    return render(request,"fifth.html",{'a':10,'b':5})