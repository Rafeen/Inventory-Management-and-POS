from django.shortcuts import render, redirect, get_object_or_404
from users.models.user_model import User
from django.contrib.auth.decorators import login_required



@login_required(login_url='/login/')
def user_detail_view(request, id):
    """
        This view renders User Detail page with a details of selected user
    """
    if request.user.is_admin:
        user_obj = get_object_or_404(User, id=id)
        context = {
            "user": user_obj,
            "title": "User Details"

        }
        return render(request, "user_detail.html", context)
    else:
        user_obj = get_object_or_404(User, id=request.user.id)
        context = {
            "user": user_obj,
            "title": "User Details"

        }
        return render(request, "user_detail.html", context)




