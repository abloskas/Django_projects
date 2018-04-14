from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^success$', views.success),
    url(r'^loading$', views.loading),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^add$', views.addBook),
    url(r'^create$', views.createBook),
    url(r'^(?P<id>\d+)$', views.showBook),
    url(r'^(?P<id>\d+)/delete$', views.deleteReview),
    url(r'^add/book-review', views.addReview),
    url(r'^users/(?P<id>\d+)$', views.userPage)
]