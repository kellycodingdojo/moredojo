from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^travels/add$', views.add),
    url(r'^main$', views.main),
    url(r'^travels$', views.travels),
    url(r'^logout$', views.logout),
    #url(r'^destination/(?P<id>\d+)$', views.dest),
     #url(r'^destination$', views.dest),
  
    url(r'^travels/add_trip$', views.add_trip),
  
]