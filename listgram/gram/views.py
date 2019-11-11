from django.shortcuts import render, redirect
from gram.models import Location, Gram, Store, Product
from gram.forms import LocationForm, StoreForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate,login,logout


from django.http import HttpResponse
def signout_view(request):
	logout(request)
	return redirect("/")
def signin_view(request):
	msg = ""
	if request.method == "POST":
		data = request.POST 
		user = authenticate(username=data.get("username"),
			password=data.get("password"))
		login(request,user)
		if user:
			msg="login successfully"
			return redirect("/gram")
		else:
			msg="Authentication Failed"
	form = AuthenticationForm()
	return render(request,"gram/signin.html",{"form":form,"msg":msg})
def signup_view(request):
	msg=""
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			msg="User Registered successfully!!"
		else:
			msg=form._errors
	else:
		form = UserCreationForm()
	return render(request,"gram/signup.html",{"form":form,"msg":msg})
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
			import pdb;pdb.set_trace()
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