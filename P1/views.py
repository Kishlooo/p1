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

def urls_data(request,name):
    return HttpResponse("<h1>{}</1>".format(name))

#def ab(request,ab):
   # a=ab.split(".")
    #sum=int(a[0]) + int(a[1])
    #return HttpResponse(str(sum))

def ab(request,a,b):
    sum=int(a)+int(b)
    return HttpResponse(str(sum))

def greater(request,c,d,e):
    if(c>d):
        if(c>e):
            return HttpResponse(c)
        else:
            return HttpResponse(e)
    else:
        if(d>e):
            return HttpResponse(d)
        else:
            return HttpResponse(e)

def strin(request,srt):
    o="aeiouAEIOU"
    vow=""
    const=""
    for i in srt:
        if i in o:
            vow+=i;
        else:
            const+=i;
    return render(request,"html/vowels.html",{'string':srt,'vowels':vow,'const':const})