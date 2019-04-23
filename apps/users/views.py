from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, "users/index.html")

def reg_form(request):
    return render(request, "users/regform.html")

def reg_process(request):
    if not User.objects.is_original("email", request.POST["email"]):
        messages.error(request, "User already exists")
        return redirect("/register")
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/register")
    new_user = User.objects.add_user(request.POST)
    request.session["userid"] = new_user.id
    messages.success(request, "Successfully registered!")
    return redirect("/dashboard")

def login_form(request):
    if "userid" in request.session:
        messages.error(request, "Already logged in!")
        return redirect("/")
    return render(request, "users/loginform.html")

def login_process(request):
    if User.objects.login(request.POST):
        request.session["userid"] = User.objects.get_id(request.POST)
        messages.success(request, "Successfully logged in!")
        return redirect("/dashboard")
    messages.error(request, "You could not be logged in")
    return redirect("/login")

def logout_process(request):
    request.session.clear()
    messages.success(request, "Logged out")
    return redirect("/")

def profile_view(request, userid):
    return render("users/profilepage.html")