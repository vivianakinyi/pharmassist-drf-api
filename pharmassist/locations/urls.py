from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns(
    '',
    url(r'^locations/$', views.LocationListView.as_view(), name='locations'),
    url(r'^locations/(?P<pk>[^/]+)/$',
        views.LocationDetailView.as_view(), name='locations'),

)
