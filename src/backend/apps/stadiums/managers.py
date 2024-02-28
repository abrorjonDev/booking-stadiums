from django.db.models import Manager, QuerySet


class StadiumManager(Manager):

    def published(self):
        """Returns only published stadiums.
        """
        return self.get_queryset().filter(
            _status=self.model.STATUS.PUBLISHED
            ).prefetch_related('bookings')
