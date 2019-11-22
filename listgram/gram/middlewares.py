from django.shortcuts import render
class ErrorMiddleWare:
	def __init__(self,view):
		self.view=view

	def __call__(self,request):
		print("before executing view")
		resp = self.view(request)
		if resp.status_code==404:
			return render(request,"gram/404.html")
		if resp.status_code==500:
			return render(request,"gram/500.html")
		
		print("before sending response")
		return resp

