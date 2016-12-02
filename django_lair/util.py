# -*- coding: utf-8 -*-
from datetime import timedelta
from django.utils import timezone


""" From a list of datums, generate a list representing frequency """
def generate_usage(data, days=30):
    start_date = timezone.now() - timedelta(days=days - 1)
    data = data.filter(created__gt=start_date).order_by('created')
    data_usage = [0] * days
    last_day = start_date.day
    index = 0
    for datum in data:
        if last_day != datum.created.day:
            index += datum.created.day - last_day
            last_day = datum.created.day
        data_usage[index] += 1
    return data_usage


def generate_day_labels(days=30):
    start_date = timezone.now() - timedelta(days=days - 1)
    return [(start_date + timedelta(i - 1)).day for i in range(days)]
