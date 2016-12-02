#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django_lair
------------

Tests for `django_lair` models module.
"""
from datetime import timedelta
from uuid import uuid4
from django.test import TestCase
from django_lair import models, util


class TestDjango_lair(TestCase):
    def setUp(self):
        self.user = models.User.objects.create(uuid=uuid4())
        self.data = []
        for i in range(40):
            datum = models.Datum.objects.create(name='test1', value=str(i), user=self.user)
            self.data.append(datum)
            datum.created -= timedelta(days=i)
            datum.save()
        pass

    def test_generate_usage_simple(self):
        extra = models.Datum.objects.create(user=self.user, name='test1', value=2)
        result, labels = util.generate_usage(models.Datum.objects.filter(name='test1'))
        self.assertEqual(len(result), 30)
        extra.delete()

    def test_generate_usage_extra(self):
        result, labels = util.generate_usage(models.Datum.objects.filter(name='test1'))
        self.assertEqual(len(result), 30)
        self.assertEqual(result[-1], 1)

        extra = models.Datum.objects.create(user=self.user, name='test1', value=2)
        result, labels = util.generate_usage(models.Datum.objects.filter(name='test1'))
        self.assertEqual(len(result), 30)
        self.assertEqual(result[-1], 2)
        extra.delete()

    def tearDown(self):
        self.user.delete()
        for datum in self.data:
            datum.delete()
