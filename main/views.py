from django.shortcuts import render


def index(reqest):
    data = {}
    return render(reqest, 'main/index.html', {'title': 'main page'})
def gallery(reqest):
    return render(reqest, 'main/gallery.html')


