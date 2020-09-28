from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    #return HttpResponse('<h1>Hello Django!</h1>')
    return render(request, 'generator/index.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    if request.GET.get('special'):
        characters.extend(list('~`!@#$%^&*()+-*/,.\|;:'))

    length = int(request.GET.get('length',8))
    upcase = request.GET.get('uppercase')
    num = request.GET.get('numbers')
    sp = request.GET.get('special')
    
    thepassword = ''
    
    for s in range(length):
        thepassword += random.choice(characters)
    
    return render(request, 'generator/password.html', {'password': thepassword})
