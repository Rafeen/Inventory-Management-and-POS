from django.shortcuts import render, redirect
from users.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
import os
from django.conf import settings
from django.core.files.storage import default_storage


@login_required(login_url='/login/')
def create_user_view(request):
    """
    This view Renders Create User Page
    """
    if request.user.is_admin:
        context = {
            "title": "Create User"
        }
        return render(request, 'create_user.html', context)
    else:
        return redirect('/dashboard/')


@login_required(login_url='/login/')
def store_user(request):
    """
    This view creates user and Store user in DB
    """
    if request.user.is_admin:
        formData = User()
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        phone = request.POST.get("phone")
        designation = request.POST.get("designation")
        isActive = request.POST.get("user_status")
        role = request.POST.get("role_id")
        if 'avatar' in request.FILES:
             avatar_file = request.FILES["avatar"]
             save_path = os.path.join(settings.MEDIA_ROOT, avatar_file.name)
             default_storage.save(save_path, avatar_file)
             formData.avatar = avatar_file.name

        formData.name = name
        formData.email = email
        formData.password = make_password(password)
        formData.phone = phone
        formData.designation = designation
        formData.status = isActive

        if isActive == 'Active':
            formData.is_active = True
        else :
            formData.is_active = False

        if role == "s":
            formData.is_staff = True
        elif role == "a" :
            formData.is_admin = True
        elif role == "v" :
            formData.is_viewer = True

        # save_path = os.path.join(settings.MEDIA_ROOT, avatar_file.name)
        # default_storage.save(save_path, avatar_file)
        #
        # formData.avatar = avatar_file.name
        formData.save()

        return redirect("/create-user/")

    else:
        return redirect('/dashboard/')
