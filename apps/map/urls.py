from django.urls import path
from . import views

# urlpatterns = [
#     url(r'^$', views.imbed),

#     url(r'^marker$', views.marker),
    
#     url(r'^add_marker$', views.add_marker),



urlpatterns = [
    path('', views.imbed),
    path('marker', views.marker),
    path('add_marker', views.add_marker),
    path('add_marker/process', views.add_marker_process),
    path('marker/<int:markerid>/view', views.read_one_marker),
    path('marker/<int:markerid>/edit', views.edit_one_marker),
    path('marker/<int:markerid>/edit/process', views.edit_one_marker_process)
]