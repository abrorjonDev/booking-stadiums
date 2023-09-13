import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def phone_number_validator(phone_number):
    pattern = re.compile(r'^998\d{9}$')

    if not pattern.match(phone_number):
        raise ValidationError(_("Invalid phone number in Uzbekistan"))
