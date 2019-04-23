from django.shortcuts import render, redirect
from .models import User, UserManager

# Create your views here.

def dashboard(request):

    return render(request, "dashboard/dashboard.html")