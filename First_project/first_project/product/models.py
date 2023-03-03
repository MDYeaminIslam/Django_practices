from django.db import models

# Create your models here.
#we'll create database to store our data

class laptop(models.Model):
    #here we are creating a table in the database
    password = models.CharField(max_length=50)
    re_password = models.CharField(max_length=50)
    laptop = models.CharField(max_length=50)
    email = models.EmailField(max_length=70)
    about = models.CharField(max_length=50)
    textarea = models.CharField(max_length=50)
    checkbox = models.CharField(max_length=50)
    ram = models.IntegerField()
    ssd = models.DecimalField(max_digits=3,decimal_places=2)
    youtube_channel = models.BooleanField(max_length=50)


