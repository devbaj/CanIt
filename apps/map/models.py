from django.db import models

class Marker(models.Model):
    lat = models.DecimalField(max_digits=7, decimal_places=4)
    lng = models.DecimalField(max_digits=7, decimal_places=4)
# Create your models here.
