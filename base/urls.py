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
    url(r'^users/$', views.UserViewSet.as_view({'get': 'list'})),
]

urlpatterns = format_suffix_patterns(urlpatterns)
