from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homeView(request):
    return render(request, 'pages/home.html')

def loginView(request):
    return render(request, 'pages/login.html')

def indexView(request):
    print("Index View")
    return render(request, 'index.html')