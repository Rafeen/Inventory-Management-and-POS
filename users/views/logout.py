from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def logout_view(request):
    """
        This view logs out User
    """
    logout(request)
    return redirect('/')
