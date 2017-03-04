from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    # url(r'^travels/add$', views.add),
    url(r'^books$', views.books),
    url(r'^send_book$', views.add_book),
    url(r'^books/add$',views.add),
    url(r'^users/(?P<id>\d+)$', views.user_info),
    url(r'^add_review$', views.add_review),
    # url(r'^travels$', views.travels),
    # url(r'^logout$', views.logout),
    url(r'^delete/(?P<id>\d+)/(?P<book_id>\d+)$', views.delete),
    url(r'^books/(?P<id>\d+)$', views.see_book),
    #  #url(r'^destination$', views.dest),
  
    # url(r'^travels/add_trip$', views.add_trip),
  
]