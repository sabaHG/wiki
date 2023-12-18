from django.shortcuts import render
from .models import Photo

def gallery(reqest):
    gallery = Photo.objects.all()
    return render(reqest, 'gallery/gallery.html',{'gallery':gallery})



