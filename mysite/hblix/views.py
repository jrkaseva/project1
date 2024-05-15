from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homeView(request):
    return render(request, 'pagess/home.html')

def loginView(request):
    return render(request, 'pages/login.html')

def indexView(request):
    return render(request, )