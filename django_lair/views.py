# -*- coding: utf-8 -*-
from django.views.generic import (
    CreateView,
    DetailView,
    ListView
)

from .models import (
    User,
    Datum,
)


class UserDetailView(DetailView):

    model = User


class UserListView(ListView):

    model = User


class DatumDetailView(DetailView):

    model = Datum


class DatumListView(ListView):

    model = Datum


class DatumCreateView(CreateView):

    model = Datum
