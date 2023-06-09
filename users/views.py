from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import CustomUserCreationForm

# Create your views here.

def login_user(request):
    page = 'login'

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            return redirect('nutritions')
        else:
            messages.error(request, "Invalid username or password")


    context = {
        'page': page
    }
    return render(request, 'users/login_register.html', context=context)




def register_user(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)
            return redirect('nutritions')
        else:
            messages.error(request, "Something went wrong")

    context = {
        'page': page,
        'form': form,
    }
    return render(request, 'users/login_register.html', context=context)



def logout_user(request):
    logout(request)

    return redirect('nutritions')