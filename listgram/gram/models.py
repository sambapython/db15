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
class Product(models.Model):
	name=models.CharField(max_length=250)

	def __str__(self):
		return self.name
class Store(models.Model):
	name = models.CharField(max_length=250)
	latitude = models.CharField(max_length=250)
	longitude = models.CharField(max_length=250)
	products = models.ManyToManyField(Product)
class Gram(models.Model):
	description = models.CharField(max_length=250) # optional field default="my shoping"
	current_location = models.ForeignKey(Location, on_delete=models.PROTECT,
	blank=True, null=True) #CASCADE
	stores=models.ManyToManyField(Store)