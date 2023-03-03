from django.db import models

# Create your models here.
#here we are going to do the database work


class pay_method(models.Model):
    #here we are going to create a class
    pay_id = models.IntegerField()
    pay_option = models.CharField(max_length=25)
    min_pay = models.IntegerField()
    
