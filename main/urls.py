from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('gallery', views.gallery, name='gallery'),
    path('character', views.character, name='character'),
]