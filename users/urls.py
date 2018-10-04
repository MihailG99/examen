from django.urls import path, include
from django.contrib import admin
from django.conf.urls import url
from . import views

urlpatterns = [
    path(r'user/', views.user_list, name="users-list"),
    ]