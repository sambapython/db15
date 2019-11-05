from gram.models import Location
from django.forms import ModelForm
class LocationForm(ModelForm):
	class Meta:
		model=Location
		fields="__all__"