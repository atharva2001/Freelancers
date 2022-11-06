from django.db import models

# Create your models here.
class Register(models.Model):
    # id = models.IntegerField(primary_key=True, editable=False, unique=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name