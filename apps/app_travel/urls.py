from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^homepage$', views.homepage , name ='home_page'),
    url(r'^destination/(?P<id>\d+)$', views.destination , name ='destination') ,
     url(r'^addlike/(?P<id>\d+)$', views.addlike , name ='addlike') ,
    url(r'^logout$', views.logout , name ='logout') ,
    url(r'^add$', views.addtravelplan , name ='add_travelplan')
    ]
     