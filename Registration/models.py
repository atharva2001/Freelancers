from django.db import models

# Registration table
class Register(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=100, default="work")

    def __str__(self):
        return self.name
