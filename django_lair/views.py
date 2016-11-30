# -*- coding: utf-8 -*-
from django.views.generic import CreateView, ListView
from django.core.urlresolvers import reverse_lazy
from .models import Datum


class DatumListView(ListView):
    model = Datum


class DatumCreateView(CreateView):
    model = Datum
    fields = ['user', 'name', 'value']
    success_url = reverse_lazy('datum_list')
