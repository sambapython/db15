# product views
from django.core.cache import cache
from django.shortcuts import render
from django.views.generic import TemplateView, DeleteView, CreateView
from gram.models import Product
def productdetailview(request,pk):
	key = "%s_%s"%("Product",pk)
	product = cache.get(key)
	if not product:
		product = Product.objects.get(id=pk)
		cache.set(key,product)
	return render(request,"gram/product_detail.html",{"object":product})
class ProductTemplateView(TemplateView):
	def get_context_data(self, **kwargs):
		data = TemplateView.get_context_data(self,**kwargs)
		data["name"]="some name"
		data["products"] = Product.objects.all()
		return data
class ProductCreateView(CreateView):
	def post(self,request,**kwargs):
		data = CreateView.post(self,request,**kwargs)
		form = self.get_form()
		inst = form.instance
		inst.user = request.user
		inst.save()
		return data

# class ProductDeleteView(DeleteView):
# 	pass
	# def get_context_data(self,**kwargs):
	# 	data = DeleteView.get_context_data(self,**kwargs)
	# 	import pdb;pdb.set_trace()