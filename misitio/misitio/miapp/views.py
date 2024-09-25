from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request,'miapp/home.html')


def about(request):
    return render(request,'miapp/about.html')


def contact(request):
    return render(request,'miapp/contact.html')

def blog(request):
    return render(request,'miapp/blog.html')

# Create your views here.
