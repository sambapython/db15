# product views
from django.views.generic import TemplateView, DeleteView
from gram.models import Product
class ProductTemplateView(TemplateView):
	def get_context_data(self, **kwargs):
		data = TemplateView.get_context_data(self,**kwargs)
		data["name"]="some name"
		data["products"] = Product.objects.all()
		return data

# class ProductDeleteView(DeleteView):
# 	pass
	# def get_context_data(self,**kwargs):
	# 	data = DeleteView.get_context_data(self,**kwargs)
	# 	import pdb;pdb.set_trace()