from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

from .forms import UserAddingForm
from .models import CustomUser


@login_required
def custom_logout(request):
    logout(request)
    return redirect("main:home")


def custom_login(request):
    if request.user.is_authenticated:
        return redirect('main:home')
    
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data["username"],
                password = form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                if request.user.is_authenticated:
                    return redirect('main:home')
        # else:
        #     for error in list(form.errors.values()):
        #         messages.error(request, 'Not login')

    form = AuthenticationForm()

    return render(request, 'users/login.html', {
        'form': form
    })


@login_required
def employess(request):
    employeeses = CustomUser.objects.all()

    return render(request, 'users/employees.html', {
        'employeeses': employeeses
    })


@login_required
def add_user(request):
    if not request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':
        form = UserAddingForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            return redirect('users:employees') 
        
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    else:
        form = UserAddingForm()
    
    return render(request, 'users/add_user.html', {
        'form': form,
    })



