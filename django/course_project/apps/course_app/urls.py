from django.conf.urls import url
from . import views


urlpatterns = [
	
	url(r'^$', views.index),
	url(r'^add_course$', views.create),
	url(r'^delete/(?P<id>\d+)$', views.delete),
	url(r'^yes/(?P<id>\d+)$', views.yes),
	url(r'^no$', views.index),
  ]