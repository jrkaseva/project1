from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from .models import Stream, Comment

# Create your views here.
def index(request):
    request.session.flush()
    request.session['username'] = None
    return render(request, 'pages/index.html')

def home(request):

    return render(request, 'pages/home.html')

def login(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            request.session['username'] = user.username
            print("User:", user.username)
            return render(request, 'pages/home.html', {'username': user.username, 'streams': Stream.objects.all(), 'comments': Comment.objects.all()})
        print("Login failed:", user)
    return redirect('/')

