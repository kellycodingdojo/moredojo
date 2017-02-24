from django.conf.urls import url
from . import views


urlpatterns = [
	
	url(r'^$', views.create),
	url(r'^ninjas/$', views.ninja),
	url(r'^ninjas/(?P<id>\w+)$', views.show),
  ]
