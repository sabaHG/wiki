from django.urls import path
from . import views

urlpatterns = [
    path('', views.character, name='character'),
    path('create', views.create, name='create'),
    path('delete/<int:id>', views.deletePers, name="delete_pers"),
]