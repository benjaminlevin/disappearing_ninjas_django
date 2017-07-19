from django.conf.urls import url
from . import views           # This line is new!

#models -- views -- templates

urlpatterns = [
  url(r'^$', views.index), 
  url(r'^ninjas$', views.all),     # This line has changed!
  url(r'^ninjas/(?P<color>\w+)$', views.show),
 ]