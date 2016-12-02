# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from model_utils.models import TimeStampedModel


@python_2_unicode_compatible
class User(models.Model):
    uuid = models.UUIDField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.uuid)


@python_2_unicode_compatible
class Datum(TimeStampedModel):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=200, db_index=True)
    value = models.TextField()

    def __str__(self):
        return str(self.user) + ' ' + self.name + ' ' + self.value + ' ' + str(self.created)
