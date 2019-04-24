from django.shortcuts import render, HttpResponse, redirect
from .models import Marker
import json




def imbed(request):

    return render(request, "map/map_imbed.html")

def marker(request):
    context = {
        'location': Marker.objects.all()
    }
    print(context)

    return render(request, 'map/marker.html', context)

def add_marker_process(request):
    print('hello_world')
    print(request.POST)
    return redirect('/add_marker')

def add_marker(request):

    return render(request, 'map/add_marker.html')