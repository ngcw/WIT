from django.conf.urls import patterns, url
from LibraryTraffic import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^mainpage/$', views.mainpage, name='mainpage'),
    url(r'^mainpage/(?P<Library_id>\d+)/$', views.detail, name='detail'),
    url(r'^mainpage/(?P<Library_id>\d+)/bookroom/$', views.bookroom, name='bookroom'),
)
