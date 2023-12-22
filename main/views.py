from django.shortcuts import render
from django.contrib.auth.models import User as CustomUser


def index(request):

    return render(request, 'index.html', {'title': 'main page'})


# def gallery(reqest):
#     return render(reqest, '/gallery.html')

def character(reqest):
    return render(reqest, 'character/character.html')


