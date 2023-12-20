from django.urls import path
from .views import register, login
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('logout/', views.logout, name='logout'),
    # path('logout/', logout, name='logout'),
]
