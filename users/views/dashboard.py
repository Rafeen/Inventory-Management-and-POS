from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def dashboard_view(request):
    """
    This view renders Dashboard
    """
    context ={
        "title": "Home"
    }
    return render(request, 'inventro_chart.html', context)
