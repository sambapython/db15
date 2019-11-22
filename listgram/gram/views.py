from django.shortcuts import render, redirect
from gram.models import Location, Gram, Store, Product
from gram.forms import LocationForm, StoreForm, UserProfileForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.views import login_required



from django.http import HttpResponse
import logging
logger = logging.getLogger(__name__)

@login_required
def findpath_view(request,pk):
	gram = Gram.objects.get(id=pk)
	current_location = gram.current_location 
	stores = gram.stores.all()
	cl_lat,cl_longi =  current_location.latitude, current_location.longitude
	stor_lat_long = [{"id":store.id,
	"lat":store.latitude,
	"long":store.longitude} for store in stores]
	print(cl_lat,cl_longi,stor_lat_long)
	#return HttpResponse("sdfs")

	'''
	write a logic to find the shortest path
	'''
	return render(request,"gram/path.html",{"gram":gram})

@login_required
def signout_view(request):
	logout(request)
	return redirect("/")
def signin_view(request):
	msg = ""
	if request.method == "POST":
		data = request.POST 
		user = authenticate(username=data.get("username"),
			password=data.get("password"))
		
		if user:
			login(request,user)
			msg="login successfully"
			return redirect("/gram")
		else:
			msg="Authentication Failed"
	form = AuthenticationForm()
	return render(request,"gram/signin.html",{"form":form,"msg":msg})
def signup_view(request):
	logger.info("signup view started")
	msg=""
	if request.method == "POST":
		form = UserProfileForm(request.POST, files=request.FILES)
		if form.is_valid():
			form.save()
			logger.info("user created")
			user=form.instance
			user.set_password(user.password)
			logger.info("password encrypted")
			user.save()
			msg="User Registered successfully!!"
		else:
			msg=form._errors
			logger.error(msg)
	else:
		form = UserProfileForm()
		logger.info("created empty user form")
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
@login_required
def gram_view(request):
	store_form = StoreForm()
	current_location_form = LocationForm()
	if request.method=="POST":
		
		data = request.POST
		gram = Gram.objects.get(id=data.get("gramid"))

		
		
		if "addstore" in data:
			store = Store(name=data.get("name"),
				latitude=data.get("latitude"),
				longitude=data.get("longitude"),
				user=request.user)
			store.save()
			
			for product_id in data.get("products"):
			     product = Product.objects.get(id=product_id)
			     store.products.add(product)
			gram.stores.add(store)
		elif "addlocation" in data:
			loc=Location(name=data.get("name"),
				latitude=data.get("latitude"),
				longitude=data.get("longitude"),
				user=request.user)
			loc.save()
			gram.current_location = loc 
			gram.save()
	else:
		gram = Gram(description="add description",user=request.user)
		gram.save()
	return render(request, "gram/gram.html",
		{"current_location_form":current_location_form,
		"store_form":store_form,
		"gram":gram})