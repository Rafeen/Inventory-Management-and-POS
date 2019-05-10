from django.shortcuts import render, redirect, get_object_or_404
from users.models.user_model import User
from django.contrib.auth.decorators import login_required
import os
from django.conf import settings
from django.core.files.storage import default_storage


@login_required(login_url='/login/')
def update_user(request):
    """
        This view changes user details and updates them
    """

    if request.user.is_admin:

        user_obj = get_object_or_404(User, id=request.POST.get("user_id"))
        print(user_obj)

        name = request.POST.get("name")
        password = request.POST.get("password")
        phone = request.POST.get("phone")
        designation = request.POST.get("designation")
        isActive = request.POST.get("user_status")
        role = request.POST.get("role_id")
       # avatar = request.POST.get("avatar")
        if 'avatar' in request.FILES:
             user_obj.avatar.delete(False)#this line deletes the previous saved pro pic
             avatar_file = request.FILES["avatar"]
             save_path = os.path.join(settings.MEDIA_ROOT, avatar_file.name)
             default_storage.save(save_path, avatar_file)
             user_obj.avatar = avatar_file.name

        user_obj.name = name
        # user_obj.email = email
        user_obj.set_password(password)
        user_obj.phone = phone
        user_obj.designation = designation
        user_obj.status = isActive
        if isActive == 'Active':
            user_obj.is_active = True
        else:
            user_obj.is_active = False

        if role == "s":
            user_obj.is_staff = True
        elif role == "a":
            user_obj.is_admin = True
        elif role == "v":
            user_obj.is_viewer = True

        # save_path = os.path.join(settings.MEDIA_ROOT, avatar_file.name)
        # default_storage.save(save_path, avatar_file)
        #
        # user_obj.avatar = avatar_file.name
        user_obj.save()

        return redirect("/users/" + str(request.POST.get('user_id')))
    else:
        return render(request, "user_detail.html")
