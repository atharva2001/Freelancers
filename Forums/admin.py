from django.contrib import admin
from .models import tags, forum, replies

# Register your models here.
admin.site.register(tags)
admin.site.register(forum)
admin.site.register(replies)
