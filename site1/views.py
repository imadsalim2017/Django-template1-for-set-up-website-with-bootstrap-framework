from django.shortcuts import render

# Create your views here.

def home(request):
    contexe = {}
    return render(request, 'home.html', {})


def profile(request):
    contexe = {}
    return render(request, 'profile.html', {})

def product(request):
    contexe = {}
    return render(request, 'product.html', {})

def contact(request):
    contexe = {}
    return render(request, 'contact.html', {})
