# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResultDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=120, null=True, blank=True)),
                ('title', models.CharField(max_length=120, null=True, blank=True)),
                ('name_of_winner', models.CharField(max_length=120, null=True, blank=True)),
                ('event', models.ForeignKey(to='results.Result')),
            ],
        ),
    ]
