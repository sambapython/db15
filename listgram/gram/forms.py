from gram.models import Location, Store, UserProfile
from django.forms import ModelForm
from django.contrib.auth.models import User

from django import forms
class UserProfileForm(ModelForm):
	class Meta:
		model=UserProfile
		fields = ["username","password","phone","pic"]
class LocationForm(ModelForm):
	class Meta:
		model=Location
		#fields="__all__"
		exclude = ["user"]

class StoreForm(ModelForm):
	class Meta:
		model=Store
		fields = ["name","latitude","longitude","products"]
	