from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.reg_form),
    path('register/process', views.reg_process)
]