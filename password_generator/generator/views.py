from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    #return HttpResponse('<h1>Hello Django!</h1>')
    return render(request, 'generator/index.html', {'password': 'abcdef14362'})

def password(request):
    return HttpResponse('<h1>Password</h1>')
