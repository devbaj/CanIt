from django.shortcuts import render, HttpResponse, redirect
from .models import Marker, User, UserManager
import json
from django.contrib import messages




def imbed(request):

    return render(request, "map/map_imbed.html")

def marker(request):
    context = {
        'location': Marker.objects.all()
    }

    return render(request, 'map/marker.html', context)

def add_marker_process(request):
    click_data = request.POST
    # print(click_data)
    newList = []
    for key in click_data:
#for every key in click_data, you want the value to be grabbed and stored as soon as it is clicked
#for ever key in click_data yo uwant the value printed  
        newList.append(click_data[key])
        # print(click_data[key])
        print("hello")
    user = User.objects.get(id=request.session["userid"])
    lat = newList[0]
    print("*"*80)
    lng = newList[1]
    print(" ")
    seed = Marker.objects.create(lat = lat, lng = lng, creator=user)
    print(seed.lat)
    print(seed.lng)



        # seed = Marker.objects.create(lat = click_data[key], lng = click_data[key])
        # print(click_data[key])
        # print(key)
    # print(seed)
        
    # click_data = request.POST
    # print(click_data)
    # print("*"*80)
    # print(click_data)
    # print(" ")

    return redirect('/map/add_marker')

def add_marker(request):

    return render(request, 'map/add_marker.html')

def read_one_marker(request, markerid):
    user = User.objects.get(id=request.session["userid"])
    this_marker = Marker.objects.get(id=markerid)
    context = {
        "user": user,
        "marker": this_marker
    }
    return render(request, 'map/viewmarkerinfo.html', context)

def edit_one_marker(request, markerid):
    if "userid" not in request.session:
        return redirect("/nolog")
    this_marker = Marker.objects.get(id=markerid)
    user = User.objects.get(id=request.session["userid"])
    if this_marker.creator != user:
        messages.error(request, "You cannot edit this marker")
        return redirect("/dashboard")
    context = {
        "marker": this_marker
    }
    return render(request, "map/editmarkerinfo.html", context)

def edit_one_marker_process(request, markerid):
    if "userid" not in request.session:
        return redirect("/nolog")
    this_marker = Marker.objects.get(id=markerid)
    user = User.objects.get(id=request.session["userid"])
    if this_marker.creator != user:
        messages.error(request, "You do not have permission to do that")
        return redirect("/dashboard")
    new_notes = request.POST["notes"]
    this_marker.notes = new_notes
    this_marker.save()
    return redirect(f"/map/marker/{markerid}/view")
