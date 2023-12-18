from .models import Pers
from django.forms import ModelForm, TextInput, FileInput, Textarea

class PersForm(ModelForm):
    class Meta:
        model = Pers
        fields = ['title', 'story', 'age', 'image']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'name'
            }),
            "story": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'about'
            }),
            "age": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'age'
            }),
            'image': FileInput(attrs={
                'class': 'form-control',
            })
        }