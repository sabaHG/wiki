from django.shortcuts import render


def chat_home(reqest):
    return render(reqest, 'chat/chat_home.html')

from django.shortcuts import render, redirect
from .models import Message
from .forms import MessageForm

def create_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('success_page')
    else:
        form = MessageForm(user=request.user)

    return render(request, 'chat/chat.html', {'form': form, "messages": Message.objects.all()})
