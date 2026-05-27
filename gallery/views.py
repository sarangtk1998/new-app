from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .models import CarImage, FlowerImage, AnimalImage


def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    
    return render(request, 'gallery/register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'gallery/login.html')


def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('login')


@login_required
def home_view(request):
    return render(request, 'gallery/home.html')


@login_required
def cars_view(request):
    cars = CarImage.objects.all()
    return render(request, 'gallery/cars.html', {'cars': cars})


@login_required
def flowers_view(request):
    flowers = FlowerImage.objects.all()
    return render(request, 'gallery/flowers.html', {'flowers': flowers})


@login_required
def animals_view(request):
    animals = AnimalImage.objects.all()
    return render(request, 'gallery/animals.html', {'animals': animals})