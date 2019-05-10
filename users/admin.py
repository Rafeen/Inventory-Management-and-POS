from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
# from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group


from .models.session import Session
from users.models import User

# Register your models here.
admin.site.unregister(Group)
admin.site.register(User)
admin.site.register(Session)


