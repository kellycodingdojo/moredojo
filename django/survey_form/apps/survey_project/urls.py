from django.conf.urls import url
from . import views


urlpatterns = [
	
	url(r'^$', views.index),
	url(r'^user_input$', views.submit_form),
  ]
