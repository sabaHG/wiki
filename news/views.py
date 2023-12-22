from django.shortcuts import render,redirect
from .models import Artiles
from .forms import ArtilesForm
from django.http import HttpResponseRedirect, HttpResponseBadRequest


def news_home(request):
    news = Artiles.objects.all()
    print(news)
    return render(request,'news/news_home.html', {'news': news})


def add_news(request):
    error = ''
    if request.method == 'POST':
        form = ArtilesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:

            data = {
                'form': form,
                'error': 'Invalid form data. Please correct the errors below.',
            }
            return render(request, 'news/add_news.html', data)
    else:
        form = ArtilesForm()

    data = {
        'form': form,
        'error': error,
    }

    return render(request, 'news/add_news.html', data)


def deletePers(request, id):
    try:
        character = Artiles.objects.get(id=id)
        character.delete()
        return redirect('news')
    except Exception as error:
        return HttpResponseBadRequest(error)