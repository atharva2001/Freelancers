from django.db import models
from datetime import datetime

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=1000)
    owner = models.CharField(max_length=1000, blank=True)
    # start_time = models.TimeField()
    # end_time = models.TimeField()
    # start_date = models.DateField()
    # end_date = models.DateField()
    def __str__(self):
        return self.name
    
class Message(models.Model):
    owner = models.CharField(max_length=1000)
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)

    def __str__(self):
        return self.user

class RoomMore(models.Model):
    name = models.CharField(max_length=1000)
    owner = models.CharField(max_length=1000, blank=True)
    start_time = models.TimeField(default=datetime.now, blank=True)
    end_time = models.TimeField(default=datetime.now, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    winner_name = models.CharField(default = "", max_length=10000)
    winner_amount = models.CharField(default = "", max_length=10000)

    def __str__(self):
        return self.name