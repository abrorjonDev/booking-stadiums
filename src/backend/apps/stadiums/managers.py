from django.db.models import Manager, QuerySet


class StadiumManager(Manager):

    def published(self):
        return self.get_queryset().filter(
            _status=self.model.STATUS.PUBLISHED
            ).prefetch_related('bookings')

    def bookable(self, start_from, till_time):
        self.published().filter(

        )