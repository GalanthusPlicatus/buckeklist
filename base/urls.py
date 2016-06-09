from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns

from base import views

urlpatterns = [
    url(r'^dream/$', views.DreamListApi.as_view(), name='dream_list'),
    url(
        r'^dream/(?P<pk>[0-9]+)/$',
        views.DreamDetailsApi.as_view(),
        name='dream_detail'
    ),

    # Users
    url(
        r'^user/$',
        views.UserViewSet.as_view({'get': 'list'}),
        name='users_list'
    ),
    url(
        r'^user/(?P<pk>[0-9]+)/$',
        views.UserViewSet.as_view({'get': 'user_details'}),
        name='user_details'
    ),
    url(
        r'^user/(?P<user_pk>[0-9]+)/dream/$',
        views.UserDreamRelation.as_view({'get': 'user_dream_list'}),
        name='user_dream_list'
    ),
    url(
        r'^user/(?P<user_pk>[0-9]+)/dream/(?P<dream_pk>[0-9]+)/$',
        views.UserDreamRelation.as_view({'get': 'user_dream_details'}),
        name='user_dream_details'
    ),

]

urlpatterns = format_suffix_patterns(urlpatterns)
