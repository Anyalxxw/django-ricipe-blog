from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
def login_views(request):
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home-page')
    else:        
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_views(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home-page')
    return render(request, 'index.html')

def signup_views(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home-page')
    else: 
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})