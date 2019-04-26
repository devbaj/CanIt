from django.db import models
from ..users.models import User, UserManager

class MarkerManager(models.Manager):
    def validation(self, postData):
        return True


class Marker(models.Model):
    lat = models.CharField(max_length=255)
    lng = models.CharField(max_length=255)
    creator = models.ForeignKey(User, related_name="creators", on_delete=models.CASCADE)
    score = models.IntegerField(default='0')
    votes = models.IntegerField(default='0')
    notes = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
# Create your models here.
