from django.db import models
from ..users.models import User, UserManager

class Marker(models.Model):
    lat = models.CharField(max_length=255)
    lng = models.CharField(max_length=255)
# Create your models here.
