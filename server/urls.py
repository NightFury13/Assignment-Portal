from django.conf.urls import patterns, include, url
from server import views
urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^(?P<course_id>[A-Z][A-Z][0-9]+)/$', views.upload, name='upload'),
)
