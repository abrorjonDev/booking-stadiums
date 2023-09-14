from django.db import models
from django.db.models.functions import Concat
from django.utils.translation import gettext_lazy as _
from django.conf import settings

from base_models import BaseModel
from stadiums.managers import StadiumManager


class Stadium(BaseModel):
    class STATUS(models.TextChoices):
        """ Status choices of Stadium object"""

        DRAFT = "draft", _("Draft")
        PUBLISHED = "published", _("Public to all")
        CLOSED = "closed", _("Closed")

    name = models.CharField(_("Stadium name"), max_length=255)
    address = models.CharField(_("Address"), max_length=500, default="")

    # it was possible to do very well, as like contacts had to be another model
    # with contact_type(like `phone_number` or `telegram` or `instagram`)
    contact = models.CharField(_("Contact"), max_length=100, default="")
    price_per_hour = models.PositiveBigIntegerField(_("Price per hour"))

    _status = models.CharField(
        _("Status"), max_length=9, choices=STATUS.choices, default=STATUS.DRAFT, db_index=True)

    # longitude = models.DecimalField(max_digits=30, decimal_places=8, null=True)
    # latitude = models.DecimalField(max_digits=30, decimal_places=8, null=True)

    objects = StadiumManager()

    class Meta:
        verbose_name = _('Stadium')
        verbose_name_plural = _('Stadiums')
        ordering = ('-modified_at', '-created_at')
    
    def __str__(self) -> str:
        return self.name

    @property
    def images_list(self):
        return self.images.only('media')
    
    def images_data(self, request):
        media_url = request.build_absolute_uri(settings.MEDIA_URL)
        return self.images_list.values('id').annotate(
            media=Concat(
                models.Value(media_url), models.F('media'), 
                output_field=models.CharField()
                )
            )

    @property
    def price_readable(self):
        return "{:,} soum".format(self.price_per_hour)

    @property
    def status(self):
        return self._status
    
    def set_status(self, status: str) -> None:
        setattr(self, '_status', status)


class StadiumImage(BaseModel):
    stadium = models.ForeignKey('stadiums.Stadium', models.CASCADE, related_name='images', db_index=True)
    media = models.ImageField(upload_to='stadiums/')

    class Meta:
        verbose_name = _('Stadium Image')
        verbose_name_plural = _('Stadium Images')

    def __str__(self) -> str:
        return self.media.name
