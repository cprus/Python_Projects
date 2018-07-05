from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.create),
    url(r'^adddesc/(?P<note_id>\d+)$', views.adddesc),
    url(r'^delete/(?P<note_id>\d+)$', views.delete)
         # This line has changed!
  ]
