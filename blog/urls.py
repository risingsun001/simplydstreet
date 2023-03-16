from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', lambda req: redirect('index')),
    path('dashboard/', views.index, name='index'),
]
