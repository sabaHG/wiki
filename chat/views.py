from django.shortcuts import render


def chat_home(reqest):
    return render(reqest, 'chat/chat_home.html')