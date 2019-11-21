"""listgram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from gram.views import fun, gram_view, signup_view, signin_view, signout_view,\
findpath_view
from django.views.generic import TemplateView,CreateView, UpdateView, DeleteView
from gram.models import Product
from gram.products import ProductTemplateView, ProductCreateView
from django.conf import settings
from django.conf.urls.static import static

#from app1.views import app1_view
'''
from django.http import HttpResponse
def fun(request):
	return HttpResponse("hello")
'''

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', fun),
    #path("app1/",app1_view),
    path("gram/",gram_view), #ErrorMiddleWare(gram_view)
    # path("signup/",signup_view)
    path("signup/",signup_view),
    path("signin/",signin_view),
    path("signout/",signout_view),
    re_path("findpath/(?P<pk>[0-9]+)",findpath_view),#findpath_view(request,pk=)
    path("products/",ProductTemplateView.as_view(
        template_name="gram/products.html"),

    ),
    path("create_product/",ProductCreateView.as_view(
        model = Product,
        fields = ["name","pic"],
        success_url="/products",
        #template_name="gram/createproduct.html"
        )),
    re_path("update_product/(?P<pk>[0-9]+)",UpdateView.as_view(
        model = Product,
        fields = ["name","pic"],
        success_url="/products",
        )),
    re_path("delete_product/(?P<pk>[0-9]+)",DeleteView.as_view(
        model = Product,
        success_url="/products",
        )),
]


urlpatterns = urlpatterns+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
