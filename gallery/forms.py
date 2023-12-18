from .models import Photo
from django.forms import ModelForm, FileInput

class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = ['image']

        widgets = {
            'image': FileInput(attrs={
                'class': 'form-control',
            })
        }