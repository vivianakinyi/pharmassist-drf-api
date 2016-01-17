from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns(
    '',
    url(r'^patients/$', views.PatientListView.as_view(), name='patients'),
    url(r'^patients/(?P<pk>[^/]+)/$',
        views.PatientDetailView.as_view(), name='patients'),

    url(r'^pharmacists/$', views.PharmacistListView.as_view(),
        name='pharmacists'),
    url(r'^pharmacists/(?P<pk>[^/]+)/$',
        views.PharmacistDetailView.as_view(), name='pharmacists'),
)
