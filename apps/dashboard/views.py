from django.shortcuts import render, redirect
from .models import User, UserManager, Marker

# Create your views here.

def dashboard(request):
    if "userid" not in request.session:
        return redirect("/nolog")
    markerlist = Marker.objects.all()
    user = User.objects.get(id=request.session["userid"])
    context = {
        "markerlist": markerlist,
        "user": user
    }
    return render(request, "dashboard/dashboard.html", context)