from django.shortcuts import render, redirect
from .models import Pers
from .forms import PersForm

def character(reqest):
    character = Pers.objects.all()
    return render(reqest, 'character/character.html',{'character':character})

def create(request):
    error = ''
    if request.method == 'POST':
        form = PersForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('character')
        else:

            data = {
                'form': form,
                'error': 'Invalid form data. Please correct the errors below.',
            }
            return render(request, 'character/create.html', data)
    else:
        form = PersForm()

    data = {
        'form': form,
        'error': error,
    }

    return render(request, 'character/create.html', data)