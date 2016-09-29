# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import categories.models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=categories.models.image_upload_to)),
                ('category', models.ForeignKey(to='categories.Category')),
            ],
        ),
    ]
