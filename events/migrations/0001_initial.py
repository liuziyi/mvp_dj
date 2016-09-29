# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=120)),
                ('start_date', models.DateField(null=True, blank=True)),
                ('end_date', models.DateField(null=True, blank=True)),
                ('venue', models.CharField(max_length=120, null=True, blank=True)),
                ('deadline', models.DateField(null=True, blank=True)),
                ('link', models.URLField(null=True, blank=True)),
            ],
            options={
                'ordering': ['start_date'],
            },
        ),
    ]
