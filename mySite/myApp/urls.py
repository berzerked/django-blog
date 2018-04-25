from django.conf.urls import url
from . import views 				#period '.' is used for importing from current package

urlpatterns = [
	url(r'^$', views.index, name='index')
	]