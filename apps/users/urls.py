from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.reg_form),
    path('register/process', views.reg_process),
    path('login', views.login_form),
    path('login/process', views.login_process),
    path('logout', views.logout_process),
    path('olog', views.not_logged),
    path('profile/view/<int:userid>', views.profile_view),
    path('profile/edit', views.edit_profile_form),
    path('profile/edit/process', views.edit_profile_process)
]