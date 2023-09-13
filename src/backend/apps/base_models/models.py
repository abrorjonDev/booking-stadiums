from django.conf import settings

from django.db import models


class BaseModel(models.Model):
    """Base class"""
    _created_by = models.ForeignKey(settings.AUTH_USER_MODEL, models.SET_NULL, null=True, related_name='+')
    _modified_by = models.ForeignKey(settings.AUTH_USER_MODEL,  models.SET_NULL, null=True, related_name='+')

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def set_created_by(self, created_by):
        setattr(self, '_created_by', created_by)
    
    def set_modified_by(self, modified_by):
        setattr(self, '_modified_by', modified_by)

    @property
    def created_by(self):
        return self._created_by

    @property
    def modified_by(self):
        return self._modified_by