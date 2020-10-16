# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
from airport.models import AirportLocation


class Customer(models.Model):
    """
    A Customer is a person interested in receiving text messages
    """
    id = models.AutoField(primary_key=True)
    phone_number = PhoneNumberField()
    # a customer can have association with many airports
    airports = models.ManyToManyField(AirportLocation, related_name='+')
    # subscribed is True when a Customer wants to receive SMS notifications
    is_subscribed = models.BooleanField(default=False)
    # amount a customer has donated to the cause
    donation_amount = models.DecimalField(decimal_places=2, max_digits=8, default=1)

    def __str__(self):
        return "<{}> {}".format(self.id, self.phone_number)

