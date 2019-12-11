# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interview_checker', '0004_auto_20191211_0444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interviewtimeslot',
            name='appointment_date',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
    ]
