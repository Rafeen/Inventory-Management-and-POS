from django.shortcuts import render,redirect
from users.models.user_model import User
from django.contrib.auth.decorators import login_required



@login_required(login_url='/login/')
def user_list_view(request):
    """
        This view renders All user page with a list of all registered user
    """
    if request.user.is_admin:
        queryset = User.objects.all()
        context = {
            "user_list": queryset,
            "title":"All Users"
        }
        return render(request, 'user_list.html', context)
    else:
        return redirect('/dashboard/')
