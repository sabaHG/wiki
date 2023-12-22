from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path("post/<slug:slug>/", views.detail, name="detail"),
    path('add', views.add, name='add'),
    path("post/<slug:slug>/add_comment/", views.add_comment, name="add_comment"),
]