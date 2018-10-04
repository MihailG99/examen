from django.shortcuts import render
from django.http import HttpResponse
from .models import Users

# Create your views here.

def user_list(request):
    all_users = Users.objects.all()

    context = {
        "all_users": all_users,
    }
    return render(request, "home.html", context)