from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from users.managers import UserManager
from users.validators import phone_number_validator


class User(AbstractUser):
    email = None
    username = None

    phone_number = models.CharField(
        _("Phone Number"),
        max_length=13, 
        validators=[phone_number_validator], 
        unique=True,
        error_messages={
            "unique": _("A user with that phone number already exists."),
        },
    )
    EMAIL_FIELD = None
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self) -> str:
        if self.last_name and self.first_name:
            return self.get_full_name()
        return self.phone_number

    @property
    def role(self):
        role = self.groups.first()
        if role:
            return role.name
