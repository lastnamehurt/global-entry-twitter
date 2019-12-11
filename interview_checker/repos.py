from __future__ import unicode_literals

from interview_checker.models import InterviewTimeSlot


class InterviewSlotRepo(object):

    def get(self, **kwargs):
        return InterviewTimeSlot.objects.get(**kwargs)

    def create(self, **kwargs):
        return InterviewTimeSlot.objects.create(**kwargs)

    def list_all(self):
        return InterviewTimeSlot.objects.all()

    def update(self, location_id, **filters):
        return InterviewTimeSlot.objects.filter(location_id=location_id).update(**filters)

    def save(self, location_id):
        model = InterviewTimeSlot.objects.get(location_id=location_id)
        model.save()
        return model

    def filter(self, **filters):
        model = InterviewTimeSlot.objects.filter(**filters)
        return model


interview_slot_repo = InterviewSlotRepo()