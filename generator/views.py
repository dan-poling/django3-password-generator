from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.


def home(request):
    return render (request, 'generator/home.html')

def password(request):
    import string
    characters = list(string.ascii_lowercase)
    length = int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        characters.extend(string.ascii_uppercase)

    if request.GET.get('numbers'):
        characters.extend( [str(x) for x in range(0,10)] )

    if request.GET.get('special'):
        from string import punctuation
        characters.extend(set(punctuation))

    thePassword = ''

    for x in range(length):
        thePassword += random.choice(characters)

    return render (request, 'generator/password.html', {'password': thePassword})

def about(request):
    return render (request, 'generator/about.html')