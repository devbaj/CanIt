from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard),
    path('up', views.vote_up),
    path('down', views.vote_down)


]