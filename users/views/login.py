from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def login_view(request):
    """
        This view renders Dashboard
        """
    if request.user.is_authenticated:
        #if User is already logged in redirects to Home Page
        return redirect("/dashboard/")

    if request.method == "POST":
        #if user is not logged in redirects to Login page
        username = request.POST.get("email")
        password = request.POST.get("password")
        remember = request.POST.get("remember")
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("/dashboard/")
            else:
                return render(request, 'login.html')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')