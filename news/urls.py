from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('add_news/', views.add_news, name='add_news'),
]