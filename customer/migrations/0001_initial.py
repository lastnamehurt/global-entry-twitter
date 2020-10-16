# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-10-16 23:05
from __future__ import unicode_literals

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('airport', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('is_subscribed', models.BooleanField(default=False)),
                ('is_enabled', models.BooleanField(default=False)),
                ('donation_amount', models.DecimalField(decimal_places=2, default=1, max_digits=8)),
                ('airports', models.ManyToManyField(related_name='_customer_airports_+', to='airport.AirportLocation')),
            ],
        ),
    ]
