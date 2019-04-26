from django.urls import path
from . import views

urlpatterns = [
    path('create/<int:markerid>', views.create_event_form),
    path('create/<int:markerid>/process', views.create_event_process),
    path('view/<int:eventid>', views.view_event),
    path('<int:eventid>/destroy', views.destroy_event),
    path('<int:eventid>/leave', views.leave_event),
    path('<int:eventid>/join', views.join_event)
]