from django.shortcuts import render

# Create your views here.
def app1_view(request):
	return render(request, "app1/index.html")
