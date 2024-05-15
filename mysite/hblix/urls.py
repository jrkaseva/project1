from django.contrib import admin
from django.urls import include, path
from .views import homeView, loginView, indexView

urlpatterns = [
    path('', indexView, name='index'),
    path('login/', loginView, name='login'),
    path('home/', homeView, name='home')
]   