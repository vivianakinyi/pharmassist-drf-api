from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns(
    '',
    url(r'^pharmacy/$', views.PharmacyListView.as_view(), name='pharmacy'),
    url(r'^pharmacy/(?P<pk>[^/]+)/$',
        views.PharmacyDetailView.as_view(), name='pharmacy'),

)
