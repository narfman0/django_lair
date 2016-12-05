# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
from django.db import migrations, models
from django.utils import timezone
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Datum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('value', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True, default=timezone.now())),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, default=timezone.now())),
                ('uuid', models.UUIDField()),
            ],
        ),
        migrations.AddField(
            model_name='datum',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_lair.User'),
        ),
    ]
