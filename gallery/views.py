from django.shortcuts import render, redirect
from .models import Photo
from .forms import PhotoForm

def gallery(request):
    gallery = Photo.objects.all()
    return render(request, 'gallery/gallery.html', {'gallery': gallery})

def add(request):
    error = ''
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery')
        else:
            data = {
                'form': form,
                'error': 'Invalid form data. Please correct the errors below.',
            }
            return render(request, 'gallery/add.html', data)
    else:
        form = PhotoForm()

    data = {
        'form': form,
        'error': error,
    }

    return render(request, 'gallery/add.html', data)