
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class InterviewTimeSlot(models.Model):
    id = models.AutoField(primary_key=True)
    location_name = models.CharField(max_length=250, blank=True, null=False)
    location_id = models.IntegerField()
    appointment_date = models.DateTimeField(auto_now=False, null=True, auto_now_add=False)
    date_changed = models.BooleanField(default=False)

    def __str__(self):
        return "{}: <{}>".format(self.location_name, self.appointment_date)

    class Meta:
        db_table = 'global_entry_appointment'
