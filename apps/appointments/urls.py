from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^create/$', views.create, name='create'),
    url(r'^edit/(?P<id>\d+)/$', views.edit, name='edit'),
    url(r'^$', views.index, name='index'),
    url(r'^delete/(?P<id>\d+)/$', views.delete, name='delete'),
]
