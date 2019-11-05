from django.shortcuts import render
from gram.models import Location
from gram.forms import LocationForm

# Create your views here.
from django.http import HttpResponse
def fun(request):
	"""
	res='''
	<html><h1>HELLO</h1></html>
	'''
	"""
	#return HttpResponse("hello")
	#return HttpResponse(res)
	return render(request, "gram/index.html")

def gram_view(request):
	if request.method=="POST":
		data = request.POST
		'''
		loc = Location(name=data.get("current_location"),
			latitude=data.get("latitude"),
			longitude=data.get("logitude"))
		loc.save()
		'''
		data._mutable=True
		data.pop("csrfmiddlewaretoken")
		loc=Location(**data)
		loc.save()
	else:
		form = LocationForm()
	return render(request, "gram/gram.html",{"form":form})