from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns(
    '',
    url(r'^pharmacy/$', views.PharmacyListView.as_view(), name='pharmacy'),
    url(r'^pharmacy/(?P<pk>[^/]+)/$',
        views.PharmacyDetailView.as_view(), name='pharmacy'),

    url(r'^drugs/$', views.DrugListView.as_view(), name='drugs'),
    url(r'^drugs/(?P<pk>[^/]+)/$',
        views.DrugDetailView.as_view(), name='drugs'),

    url(r'^prices/$', views.PriceListView.as_view(), name='prices'),
    url(r'^prices/(?P<pk>[^/]+)/$',
        views.PriceDetailView.as_view(), name='prices'),

)
