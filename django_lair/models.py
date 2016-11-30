# -*- coding: utf-8 -*-

from django.db import models
from model_utils.models import TimeStampedModel


class User(models.Model):
    uuid = models.UUIDField()


class Datum(TimeStampedModel):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=200, db_index=True)
    value = models.TextField()
