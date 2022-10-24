from django.shortcuts import render,redirect
from .models import Product
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
from django.views.decorators.cache import cache_control

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def login(request):
    if 'user' in request.session:
        return redirect('login')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            request.session['user']=username
            return redirect('home')
        else:
            messages.error(request,'Invalid username or password')
            return redirect('login')
    return render(request,'blog/login.html')
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def home(request):
    products={
        'items': Product.objects.all(),
    }
    if 'user' in request.session:
        return render(request,'blog/home.html',products)
    return redirect('login')
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def logout(request):
    if 'user' in request.session:
        request.session.flush()
    return redirect('login')