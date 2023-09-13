from django.db import models
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _

from base_models import BaseModel


class Booking(BaseModel):
    class STATUS(models.TextChoices):
        PENDING = 'pending', _('PENDING')
        APPROVED = 'approved', _('APPROVED')
        DECLINED = 'declined', _('DECLINED')
        ARCHIVED = 'archived', _('ARCHIVED')

    stadium = models.ForeignKey('stadiums.Stadium', models.CASCADE, related_name='bookings', db_index=True)
    _status = models.CharField(_('STATUS'), max_length=8, choices=STATUS.choices, default=STATUS.PENDING)

    booked_at = models.DateTimeField(_('order booked at'))
    closed_at = models.DateTimeField(_('order closed at'))

    _cost = models.PositiveBigIntegerField(_('cost'), default=0)

    class Meta:
        verbose_name = _('Booking')
        verbose_name_plural = _('Booking')
        ordering = ('-modified_at', '-created_at')

    def __str__(self) -> str:
        return "%s stadium was booked from %s till %s" % (str(self.stadium), self.booked_at, self.closed_at)

    @cached_property
    def hours(self):
        dt = self.closed_at - self.booked_at
        return dt.hours

    @property
    def cost(self):
        return self._cost
    
    def set_cost(self, cost: int):
        setattr(self, '_cost', cost)
    
    @property 
    def status(self):
        return self._status
    
    def set_status(self, status: int):
        setattr(self, '_status', status)