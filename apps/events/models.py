from django.db import models
from ..map.models import User, UserManager, Marker, MarkerManager

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=45)
    date = models.DateField()
    time = models.TimeField()
    notes = models.TextField()
    host = models.ForeignKey(User, related_name="hosts", on_delete=models.CASCADE)
    spot = models.ForeignKey(Marker, related_name="spots", on_delete=models.CASCADE)
    attendee = models.ManyToManyField(User, related_name="attendees")