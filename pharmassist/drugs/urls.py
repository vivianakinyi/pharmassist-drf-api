from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns(
    '',
    url(r'^drugs/$', views.DrugListView.as_view(), name='drugs'),
    url(r'^drugs/(?P<pk>[^/]+)/$',
        views.DrugDetailView.as_view(), name='drugs'),
)
