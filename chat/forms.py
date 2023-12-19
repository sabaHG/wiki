from django import forms
from django.contrib.auth import get_user_model
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['text', 'author']
        widgets = {
            'author': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(MessageForm, self).__init__(*args, **kwargs)

        # Если пользователь предоставлен, установите его в качестве начального автора
        if user:
            self.fields['author'].initial = user

    def clean_author(self):
        # Гарантировать, что поле автора не может быть изменено на клиентской стороне
        return self.instance.author
