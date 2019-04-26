from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.

def create_event_form(request, markerid):
    if "userid" not in request.session:
        return redirecet("/nolog")
    this_marker = Marker.objects.get(id=markerid)
    this_user = User.objects.get(id=request.session["userid"])
    context = {
        "marker": this_marker
    }
    return render(request, "events/createeventform.html", context)

def create_event_process(request, markerid):
    if "userid" not in request.session:
        return redirect("/nolog")
    this_marker = Marker.objects.get(id=markerid)
    this_user = User.objects.get(id=request.session["userid"])
    new_event = Event.objects.create(
        title = request.POST["title"],
        date = request.POST["date"],
        time = request.POST["time"],
        notes = request.POST["notes"],
        host = this_user,
        spot = this_marker
    )
    return redirect(f"/events/view/{new_event.id}")

def view_event(request, eventid):
    this_event = Event.objects.get(id=eventid)
    this_user = User.objects.get(id=request.session["userid"])
    context = {
        "event": this_event,
        "user": this_user
    }
    return render(request, "events/eventinfo.html", context)

def destroy_event(request, eventid):
    if "userid" not in request.session:
        return redirect("/nolog")
    this_event = Event.objects.get(id=eventid)
    this_user = User.objects.get(id=request.session["userid"])
    if this_user != this_event.host:
        messages.error(request, "You can't delete this event!")
        return redirect("/dashboard")
    this_event.delete()
    messages.success(request, "Event removed")
    return redirect("/dashboard")


def leave_event(request, eventid):
    if "userid" not in request.session:
        return redirect("/nolog")
    this_event = Event.objects.get(id=eventid)
    this_user = User.objects.get(id=request.session["userid"])
    if this_user not in this_event.attendees:
        messages.error(request, "You are the host!")
        return redirect("/dashboard")
    this_event.attendees.remove(this_user)
    messages.success(request, "You have left the event")
    return redirect("/dashboard")

def join_event(request, eventid):
    if "userid" not in request.session:
        return redirect("/nolog")
    this_event = Event.objects.get(id=eventid)
    this_user = User.objects.get(id=request.session["userid"])
    if this_user in this_event.attendees:
        messages.error(request, "You already joined!")
        return redirect("/dashboard")
    this_event.attendees.add(this_user)
    messages.success(request, "You have joined the event")
    return redirect("/dashboard")