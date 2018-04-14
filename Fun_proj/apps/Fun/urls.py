from django.shortcuts import render, redirect
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^wish_items/dashboard$', views.dashboard),
    url(r'^loading$', views.loading),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^wish_item/add_item$', views.add_item),
    url(r'^wish_item/create$', views.create),
    url(r'^wish_items/(?P<id>\d+)/delete$', views.delete),
    url(r'^wish_items/(?P<id>\d+)/add$', views.add),
    url(r'^wish_items/(?P<id>\d+)/remove$', views.remove),
    url(r'^wish_items/(?P<id>\d+)$', views.item)
]