from django.shortcuts import render, redirect
from .models import User, UserManager, Marker, Event

# Create your views here.

def dashboard(request):
    if "userid" not in request.session:
        return redirect("/nolog")
    markerlist = Marker.objects.all()
    user = User.objects.get(id=request.session["userid"])
    events = Event.objects.all()
    context = {
        "markerlist": markerlist,
        "user": user,
        "events": events
    
    }
    return render(request, "dashboard/dashboard.html", context)

def vote_up(request):
    this_marker = Marker.objects.get(id=request.POST['markerid'])
    this_marker.score += 1
    this_marker.votes += 1
    this_marker.save()
    return redirect('/dashboard')

def vote_down(request):
    this_marker = Marker.objects.get(id=request.POST['markerid'])
    this_marker.score -= 1
    this_marker.votes += 1
    this_marker.save()
    return redirect('/dashboard')