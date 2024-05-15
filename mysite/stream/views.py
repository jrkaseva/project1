from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the stream index.")

def home(request):
    return render(request, 'stream/home.html')

def login(request):
    return render(request, 'stream/login.html')

def signup(request):
    return render(request, 'stream/signup.html')

