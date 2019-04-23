from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.imbed),

    url(r'^marker$', views.marker),
    
    url(r'^add_marker$', views.add_marker),


]