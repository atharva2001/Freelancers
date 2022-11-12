from django.db import models
from datetime import datetime

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=1000)
    # start_time = models.TimeField()
    # end_time = models.TimeField()
    # start_date = models.DateField()
    # end_date = models.DateField()
    
class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)

class RoomMore(models.Model):
    name = models.CharField(max_length=1000)
    start_time = models.TimeField(default=datetime.now, blank=True)
    end_time = models.TimeField(default=datetime.now, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    winner_name = models.CharField(default = "", max_length=10000)
    winner_amount = models.CharField(default = "", max_length=10000)