from .models import Artiles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArtilesForm(ModelForm):
    class Meta:
        model = Artiles
        fields = ['title', 'full_text', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'news name'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'date'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'full text'
            })
        }