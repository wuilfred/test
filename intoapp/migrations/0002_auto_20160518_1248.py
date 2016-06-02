# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saveticketevent',
            name='end_time_event',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='saveticketevent',
            name='start_time_event',
            field=models.DateTimeField(),
        ),
    ]
