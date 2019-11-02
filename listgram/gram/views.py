from django.shortcuts import render

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
	return render(request, "gram/index.html")