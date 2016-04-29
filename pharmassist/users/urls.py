from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns(
    '',
    url(r'^users/$', views.UserListView.as_view(), name='user'),
    url(r'^users/(?P<pk>[^/]+)/$',
        views.UserDetailView.as_view(), name='user'),

    url(r'^group/$', views.GroupListView.as_view(), name='group'),
    url(r'^group/(?P<pk>[^/]+)/$',
        views.GroupDetailView.as_view(), name='group'),
)
