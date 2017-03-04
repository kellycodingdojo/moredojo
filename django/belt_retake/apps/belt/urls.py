from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.forward),
    url(r'^main$', views.main),
    # url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^friends$', views.friends),
    url(r'^display$', views.display),
    url(r'^logout$', views.logout),
    url(r'^home$', views.home),
    url(r'^add_friend/(?P<id>\d+)$', views.add_friend),
    ]