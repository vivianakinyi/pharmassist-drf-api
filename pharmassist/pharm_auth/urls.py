from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns(
    '',
    url(r'^users/$', views.UserListView.as_view(), name='users'),
    url(r'^users/(?P<pk>[^/]+)/$',
        views.UserDetailView.as_view(), name='users'),

)
