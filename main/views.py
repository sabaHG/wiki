from django.shortcuts import render
from registration.models import CustomUser


def index(reqest):
    data = {}
    auth = reqest.user.id
    if auth:
        user = CustomUser.objects.get(id=auth)
        return render(reqest, 'main/index.html', {'title': 'main page', "user": user})

    return render(reqest, 'main/index.html', {'title': 'main page'})


def gallery(reqest):
    return render(reqest, 'main/gallery.html')

def character(reqest):
    return render(reqest, 'character/character.html')


