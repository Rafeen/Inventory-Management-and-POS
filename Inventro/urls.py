"""Inventro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from users.views.dashboard import dashboard_view
from users.views.login import login_view
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view
from django.contrib.auth import views as auth_views

# Django REST Swagger
# get_swagger_view: produce a schema view which uses common settings

schema_view = get_swagger_view(title='API')


urlpatterns = [
    # Admin URLs
    path('admin/', admin.site.urls,name='admin'),

    # User URLs
    path('',include("users.urls")),

    #Registration Login URLs
    path('',login_view,name='login'),

    # Inventory URLs
    path('', include('product.urls')),

    # Sales URLs
    path('', include('sales.urls')),

    # Swagger URLs
    url('docs/', schema_view),

    # API URLs
    path('api-auth/',include('rest_framework.urls')),

    # Password Reset
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_email.html'),
         name='password_reset'),

    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
         name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),



]
