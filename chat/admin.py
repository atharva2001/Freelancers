from django.contrib import admin
from .models import Room, Message, RoomMore

# Register your models here.
admin.site.register(Room)
admin.site.register(Message)
admin.site.register(RoomMore)