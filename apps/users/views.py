from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render(request, "users/index.html")

def reg_form(request):
    return render(request, "users/regform.html")

def reg_process(request):
    #if fail
    return redirect('/register')
    #else
    return redirect('/dashboard')