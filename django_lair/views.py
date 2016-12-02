# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse_lazy, reverse
from django.http.response import HttpResponseRedirect
from django.views.generic import CreateView, DetailView, ListView
from .models import Datum, User
from .util import generate_day_labels, generate_usage


class DatumListView(ListView):
    model = Datum


class DatumCreateView(CreateView):
    model = Datum
    fields = ['user', 'name', 'value']
    success_url = reverse_lazy('datum_list')

    def post(self, request, *args, **kwargs):
        if 'uuid' in request.POST:
            uuid = request.POST['uuid']
            user, created = User.objects.get_or_create(uuid=uuid)
            Datum.objects.create(user=user, name=request.POST['name'], value=request.POST['value'])
            return HttpResponseRedirect(reverse('datum_list'))
        return super(DatumCreateView, self).post(self, request, *args, **kwargs)


class DatumDetailView(DetailView):
    model = Datum

    def get_context_data(self, **kwargs):
        context = super(DatumDetailView, self).get_context_data(**kwargs)
        context['datums'] = Datum.objects.filter(name=self.get_object().name)
        return context


class UserDetailView(DetailView):
    model = User

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        context['datums'] = Datum.objects.filter(user=self.get_object())
        context['activity'] = generate_usage(Datum.objects.filter(user=self.get_object()))
        context['labels'] = generate_day_labels()
        return context
