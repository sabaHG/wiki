from django.shortcuts import render,redirect
from .models import Artiles
from .forms import ArtilesForm

def news_home(request):
    news = Artiles.objects.all()
    return render(request,'news/news_home.html', {'news': news})


def add_news(request):
    error = None
    if request.method == 'POST':
        form = ArtilesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news')
    else:
        error = 'error'

    form = ArtilesForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/add_news.html', data)