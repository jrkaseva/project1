from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    request.session.flush()
    request.session['username'] = None
    return render(request, 'pages/index.html')

def home(request):
    if request.method == 'GET':
        if request.session['username'] == 'admin':
            return render(request, 'pages/home.html', {'username': request.session['username']})
    return redirect('/')

def login(request):
    if request.method == 'POST':
        # TODO: This works, swap into a database (with no sql-injection protection)
        if request.POST['username'] == 'admin' and request.POST['password'] == 'admin':
            request.session['username'] = request.POST['username']
            return redirect('/home')
    return redirect('/')

