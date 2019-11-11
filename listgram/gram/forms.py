from gram.models import Location, Store
from django.forms import ModelForm
from django.contrib.auth.models import User
class LocationForm(ModelForm):
	class Meta:
		model=Location
		fields="__all__"

class StoreForm(ModelForm):
	class Meta:
		model=Store
		fields = "__all__"
	