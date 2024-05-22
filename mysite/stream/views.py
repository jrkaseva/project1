from django.shortcuts import render, redirect
#from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from .models import Stream, Comment, User

def index(request):
    request.session['username'] = None
    return render(request, 'pages/index.html')

"A7 IDENTIFICATION AND AUTHENTICATION FAILURES - SESSION FIXATION"
# When a user backtracks to the login page, the session is not reset
def home(request):
    if request.session['username'] is not None:
        username = request.session['username']
        return render(request, 'pages/home.html', {'username': username, 'streams': Stream.objects.all(), 'comments': Comment.objects.all()})
    return redirect('/')

"""A5 SECURITY MISCONFIGURATION - CSRF DISABLED"""
# Unsafe since CSRF protection is disabled.
@csrf_exempt
def login(request):
    request.session['username'] = None
    if request.method == 'POST':
        """A3 INJECTION"""
        # SQL INJECTION using raw SQL query, getting user from stream_user table
        # Injections must have one row returned to login
        # Easiest way to get in is limiting the results to 1 row
        # Example 1: username: "admin' --" logs in as admin. Password doesn't matter
        # Example 2: username: "' OR 1=1 LIMIT 1; --" logs in as first user in the table
        user = User.objects.raw("SELECT * FROM stream_user WHERE username = '" + request.POST['username'] + "' AND password = '" + request.POST['password']+ "'")
        
        if len(user) == 0:
            return render(request, 'pages/index.html', {'error': 'Incorrect username or password'})

        if len(user) == 1:
            user = user[0]
            request.session['username'] = user.username
            return redirect('/home', {'username': user.username, 'streams': Stream.objects.all(), 'comments': Comment.objects.all()})
        
        # SQL-INJECTION COUNTERMEASURE with ORM. Have users in auth_user table
        """
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            request.session['username'] = user.username
            print("User:", user.username)
            return render(request, 'pages/home.html', {'username': user.username, 'streams': Stream.objects.all(), 'comments': Comment.objects.all()})       
        """

        """A4 INSECURE DESIGN"""
        # Insecure design since it returns information about the number of users returned
        return render(request, 'pages/index.html', {'error': f'Error with login query: too many users returned ({len(user)})'})
    return redirect('/')

