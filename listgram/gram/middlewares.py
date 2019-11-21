class ErrorMiddleWare:
	def __init__(self,view):
		self.view=view

	def __call__(self,request):
		print("before executing view")
		resp = self.view(request)
		if resp.status_code=="404":
			return render(request,"gram/404.html")
		print("before sending response")
		return resp

