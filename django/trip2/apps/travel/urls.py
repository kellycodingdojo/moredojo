from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^main$', views.index),
    url(r'^display$', views.display),
    url(r'^logout$', views.logout),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^travels$', views.travel_dash),
    url(r'^travels/add$', views.travel_form),
    url(r'^add_trip$', views.add_trip),
    url(r'^travels/destination/(?P<id>\d+)$', views.destination),
    url(r'^travels/destination$', views.destination),
    url(r'^join/(?P<id>\d+)$', views.joins),

    ]

