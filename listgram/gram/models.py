from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
	phone = models.CharField(max_length=15, blank=True, null=True)
	pic = models.ImageField(blank=True,null=True)


# Create your models here.
class NameAbstract(models.Model):
	#abstract model: it will not create a table in the database
	# if you put this calss as a parent class to any model, then
	# that model also have the name column
	name = models.CharField(max_length=250, blank=True, null=True)

	class Meta:
		abstract=True

class Person(NameAbstract):
	#name = models.CharField(max_length=250)
	email = models.CharField(max_length=250)
	phone = models.CharField(max_length=17)
	age = models.IntegerField()
class Location(NameAbstract):
	#name=models.CharField(max_length=250)
	latitude = models.CharField(max_length=20)
	longitude=models.CharField(max_length=20)
	user = models.ForeignKey(UserProfile, on_delete=models.PROTECT)

	def __str__(self):
		return "%s->%s,%s"%(self.name,self.latitude,self.longitude)
class Product(NameAbstract):
	#name=models.CharField(max_length=250)
	user = models.ForeignKey(UserProfile, on_delete=models.PROTECT,
		blank=True, null=True)
	pic = models.ImageField(blank=True,null=True)

	def __str__(self):
		return self.name
class Store(NameAbstract):
	#name = models.CharField(max_length=250)
	latitude = models.CharField(max_length=250)
	longitude = models.CharField(max_length=250)
	products = models.ManyToManyField(Product)
	user = models.ForeignKey(UserProfile, on_delete=models.PROTECT)
class Gram(models.Model):
	description = models.CharField(max_length=250) # optional field default="my shoping"
	current_location = models.ForeignKey(Location, on_delete=models.PROTECT,
	blank=True, null=True) #CASCADE
	stores=models.ManyToManyField(Store)
	user = models.ForeignKey(UserProfile, on_delete=models.PROTECT)

	def __str__(self):
		return self.current_location


'''
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
'''