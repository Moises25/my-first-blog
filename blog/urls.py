from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.post_list), #ruta hacia la vista post_list
        url (r'^post/(?P<pk>[0-9]+)/$', views.post_detail), #lo que se llame post/ y tenga un numero y / redirige a la vista post_detail
        url(r'^post/new/$', views.post_new, name='post_new'), #ruta hacia la vista post_new
        url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
        ]
