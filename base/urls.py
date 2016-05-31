from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns

from base import views

urlpatterns = [
    url(r'^api/', views.DreamListApi.as_view()),
    url(r'^api/(?P<pk>[0-9]+)/$', views.DreamDetailsApi.as_view()),

    # Users
    url(r'^api/users/$', views.UserListApi.as_view()),



]

urlpatterns = format_suffix_patterns(urlpatterns)
