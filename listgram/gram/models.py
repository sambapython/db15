from django.db import models

# Create your models here.

class Person(models.Model):
	name = models.CharField(max_length=250)
	email = models.CharField(max_length=250)
	phone = models.CharField(max_length=17)
	age = models.IntegerField()
class Location(models.Model):
	name=models.CharField(max_length=250)
	latitude = models.CharField(max_length=20)
	longitude=models.CharField(max_length=20)