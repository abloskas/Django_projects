from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^form$', views.form),
    url(r'^logout$', views.logout)
]