from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Pers
from .forms import PersForm
from django.http import HttpResponseRedirect, HttpResponseBadRequest


def character(request):
    characters = Pers.objects.all()
    return render(request, 'character/character.html', {"characters": characters})


@login_required
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

@login_required
def deletePers(request, id):
    try:
        character = Pers.objects.get(id=id)
        character.delete()
        return redirect('character')
    except Exception as error:
        return HttpResponseBadRequest(error)