from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^dashboard$', views.dash),
    url(r'^wish_items/create$', views.add_item),
    url(r'^add_product$', views.add_product),
    # url(r'^home$', views.home),
    url(r'^show_product/(?P<id>\d+)$', views.show_product),
    url(r'^dashboard/(?P<id>\d+)$', views.add_wish),
    url(r'^logout$', views.logout),
    url(r'^remove/(?P<id>\d+)$', views.remove),
    url(r'^delete/(?P<id>\d+)$', views.delete)
]