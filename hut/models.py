from django.db import models


# Create your models here.
class Huts(models.Model):
    hutname = models.CharField(max_length=128)
    image = models.ImageField(upload_to='hut/pictures')
    altitude = models.IntegerField()
    mountain = models.CharField(max_length=64)
    people_capacity = models.IntegerField()
    email = models.EmailField()
    phone = models.IntegerField()
