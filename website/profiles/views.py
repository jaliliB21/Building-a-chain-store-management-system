from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def profile(reuqest):
    if not reuqest.user.is_authenticated:
        return redirect('/')
    
    return render(reuqest, 'profiles/profile.html')