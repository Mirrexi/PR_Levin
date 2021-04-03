from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render  (request, 'main/main_page.html')

def about(request):
    return render (request, 'main/about.html')

def contact(request):
    return render (request, 'main/contact.html',{'values' : ["first","second"]})

def FAQ(request):
    return render (request, 'main/FAQ.html')

def Emperor(request):
    return render (request, 'main/Emperor.html')

def Vader(request):
    return render (request, 'main/Vader.html')

def Tarkin(request):
    return render (request, 'main/Tarkin.html')