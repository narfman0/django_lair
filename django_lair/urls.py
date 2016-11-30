# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views


urlpatterns = [
    url(
        regex="^User/(?P<pk>\d+)/$",
        view=views.UserDetailView.as_view(),
        name='User_detail',
    ),
    url(
        regex="^User/$",
        view=views.UserListView.as_view(),
        name='User_list',
    ),
    url(
        regex="^Datum/(?P<pk>\d+)/$",
        view=views.DatumDetailView.as_view(),
        name='Datum_detail',
    ),
    url(
        regex="^Datum/$",
        view=views.DatumListView.as_view(),
        name='Datum_list',
    ),
    url(
        regex="^Datum/create/$",
        view=views.DatumCreateView.as_view(),
        name='Datum_create',
    ),
]
