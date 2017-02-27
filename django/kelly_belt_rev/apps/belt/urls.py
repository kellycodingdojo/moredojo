from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    # url(r'^travels/add$', views.add),
    url(r'^books$', views.books),
    url(r'^books/add$', views.add),
    url(r'^book_view$', views.see_book),
    #url(r'^add$', views.add),
    # url(r'^travels$', views.travels),
    # url(r'^logout$', views.logout),
    # url(r'^books/(?P<id>\d+)$', views.view_book),
    #  #url(r'^destination$', views.dest),
  
    # url(r'^travels/add_trip$', views.add_trip),
  
]