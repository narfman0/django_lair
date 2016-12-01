# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from . import views


urlpatterns = [
    url(
        regex="^datum/$",
        view=views.DatumListView.as_view(),
        name='datum_list',
    ),
    url(
        regex="^datum/create/$",
        view=csrf_exempt(views.DatumCreateView.as_view()),
        name='datum_create',
    ),
    url(
        regex="^datum/(?P<pk>\d+)/$",
        view=views.DatumDetailView.as_view(),
        name='datum_detail',
    ),
    url(
        regex="^user/(?P<pk>\d+)/$",
        view=views.UserDetailView.as_view(),
        name='user_detail',
    ),
]
