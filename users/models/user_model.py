from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.contrib.auth.models import (
        BaseUserManager,
        AbstractBaseUser
    )

#Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user( email, password=password)
        user.is_admin=True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(unique=True, verbose_name='email address')
    name = models.CharField(max_length=40)
    phone = models.CharField(max_length=20, blank=False)
    avatar = models.ImageField(upload_to='images', blank=True)
    status = models.CharField(max_length=15, null=False)
    designation = models.CharField(max_length=40, null=False, default='Designation not set')

    created_by = models.CharField(max_length=40, blank=True)
    updated_by = models.CharField(max_length=40, blank=True)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_viewer = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, module):
        return True

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse("users:user-detail", kwargs={"id": self.id})

        #return "/users/%i/" % self.id






