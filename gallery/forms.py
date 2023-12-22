from .models import Comment, Photo
from django.forms import ModelForm, FileInput, Textarea

class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = ["name", "slug", "image"]

        widgets = {
            'image': FileInput(attrs={
                'class': 'form-control',
            })
        }



class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': Textarea(attrs={'cols': 80, 'rows': 3}),
        }
