from django.shortcuts import render
from .models import Pers

def character(reqest):
    character = Pers.objects.all()
    return render(reqest, 'character/character.html',{'character':character})
