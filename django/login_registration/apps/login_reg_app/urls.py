from django.conf.urls import url
from . import views


urlpatterns = [
	
	url(r'^$', views.index),
	url(r'^register$', views.register),
	url(r'^login$', views.login),
	# url(r'^success$', views.results),
	# url(r'^delete/(?P<id>\d+)$', views.delete),
	# url(r'^yes/(?P<id>\d+)$', views.yes),
	# url(r'^no$', views.index),
  ]