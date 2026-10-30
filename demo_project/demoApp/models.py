from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100,null= True,blank = True)
    age = models.IntegerField()
    place = models.CharField(max_length=100,null=True,blank=True)
    contact = models.CharField(max_length=15,null=True,blank=True)
    email = models.EmailField(max_length=200,null = True,blank=True)
    designation = models.CharField(max_length=100,null=True,blank=True)
    company = models.CharField(max_length=100,null=True,blank=True)

class Donordb(models.Model):
    Donor_name = models.CharField(max_length=100)
    age = models.IntegerField()
    blood_group = models.CharField(max_length=5)
    last_donation = models.DateField()

