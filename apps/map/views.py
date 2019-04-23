from django.shortcuts import render
from .models import Marker

def imbed(request):

    return render(request, "map/map_imbed.html")

def marker(request):
    context = {
        'location': Marker.objects.all()
    }
    print(context)

    return render(request, 'map/marker.html', context)

def add_marker(request):
    return render(request, 'map/add_marker.html')