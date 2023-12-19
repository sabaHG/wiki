from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from .forms import CustomUserCreationForm



def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Можно добавить дополнительные действия после успешной регистрации
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            # Можно добавить дополнительные действия после успешного входа
            return redirect('home')  # Замените 'home' на URL вашей домашней страницы
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})




