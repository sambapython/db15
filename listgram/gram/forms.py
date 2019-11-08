from gram.models import Location, Store
from django.forms import ModelForm
class LocationForm(ModelForm):
	class Meta:
		model=Location
		fields="__all__"
class StoreForm(ModelForm):
	class Meta:
		model=Store
		fields = "__all__"