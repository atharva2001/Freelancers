from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

# Create your models here.
class tags(models.Model):
   name = models.CharField(max_length=100)
   content = models.CharField(max_length=1000)
   
   def __str__(self):
      return self.name
   
class forum(models.Model):
   email = models.CharField(max_length=100, blank=True)
   title = models.CharField(max_length=1000)
   tags = models.CharField(max_length=1000)
   author_name = models.CharField(max_length=100)
   description = RichTextField(blank=True, null=True)
   date = models.DateTimeField(default=datetime.now, blank=True, null=True )
   image = models.ImageField( 
               upload_to='media/',
               null=True,
               blank=False,
               )

   def __str__(self):
      return str(self.id)
   
class replies(models.Model):
   forum_id = models.IntegerField()
   author_name = models.CharField(max_length=100)
   answer = RichTextField(blank=True, null=True)
   date = models.DateTimeField(default=datetime.now, blank=True)
   image = models.ImageField( 
               upload_to='media/',
               null=True,
               blank=False,
               )

   def __str__(self):
      return str(self.id)