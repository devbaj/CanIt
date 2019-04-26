from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, "users/index.html")

def reg_form(request):
    return render(request, "users/regform.html")

def reg_process(request):
    errors = User.objects.full_validation(request.POST)
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

def not_logged(request):
    messages.error(request, "Not logged in")
    return redirect("/")

def profile_view(request, userid):
    if "userid" not in request.session:
        return redirect("/nolog")
    user = User.objects.get(id=request.session["userid"])
    context = {
        "user": user
    }
    return render(request, "users/profilepage.html", context)

def edit_profile_form(request):
    if "userid" not in request.session:
        return redirect("nolog")
    user = User.objects.get(id=request.session["userid"])
    context = {
        "user": user
    }
    return render(request, 'users/profileeditform.html', context)

def edit_profile_process(request):
    if "userid" not in request.session:
        return redirect("/nolog")
    errors = User.objects.edit_validation(request.session["userid"],request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/profile/edit")
    User.objects.update(request.session["userid"], request.POST)
    messages.success(request, "Info updated!")
    return redirect(f"/profile/view/{request.session['userid']}")

def header(request):
    return render(request, "users/partials/header.html")

def footer(request):
    return render(request, "users/partials/footer.html")

def sidebar(request):
    return render(request, "users/partials/sidebar.html")