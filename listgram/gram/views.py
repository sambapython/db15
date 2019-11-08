from django.shortcuts import render
from gram.models import Location, Gram, Store, Product
from gram.forms import LocationForm, StoreForm

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
	store_form = StoreForm()
	current_location_form = LocationForm()
	if request.method=="POST":
		
		data = request.POST
		gram = Gram.objects.get(id=data.get("gramid"))
		
		if "addstore" in data:
			store = Store(name=data.get("name"),
				latitude=data.get("latitude"),
				longitude=data.get("longitude"))
			store.save()
			for product_id in data.get("products"):
			     product = Product.objects.get(id=product_id)
			     store.products.add(product)
			gram.stores.add(store)
		elif "addlocation" in data:
			loc=Location(name=data.get("name"),
				latitude=data.get("latitude"),
				longitude=data.get("longitude"))
			loc.save()
			gram.current_location = loc 
			gram.save()
	else:
		gram = Gram(description="add description")
		gram.save()
	return render(request, "gram/gram.html",
		{"current_location_form":current_location_form,
		"store_form":store_form,
		"gram":gram})