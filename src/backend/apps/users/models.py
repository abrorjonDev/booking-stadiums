from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from users.managers import UserManager
from users.validators import phone_number_validator


class User(AbstractUser):
    class ROLE(models.TextChoices):
        ADMIN = 'admin', _("Admin")
        STADIUM_OWNER = 'owner', _("Stadium Owner")
        USER = 'user', _("User")

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
    _role = models.CharField(max_length=5, choices=ROLE.choices, default=ROLE.USER)
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
        return self._role

    def set_role(self, role):
        setattr(self, '_role', role)
