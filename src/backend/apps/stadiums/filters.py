import django_filters
from django.db import models
from django_filters import rest_framework as filters

from stadiums.models import Stadium


class StadiumListFilter(filters.FilterSet):
    """Filters a list of user's stadiums
    """

    status = django_filters.ChoiceFilter(field_name='_status',
                                         lookup_expr='exact',
                                         choices=Stadium.STATUS.choices)

    class Meta:
        model = Stadium
        fields = []


class StadiumSearchFilter(filters.FilterSet):
    """
        Filters for users who want to book a stadium
    """
    booked_at = django_filters.DateTimeFilter(
        method='filter_datetime_in',
        input_formats=['%d-%m-%Y %H:%M:%S', '%Y-%m-%d %H:%M'],
        label='Enter a date/time (e.g., YYYY-MM-DD HH:MM:SS)',
    )
    closed_at = django_filters.DateTimeFilter(
        method='filter_datetime_in',
        input_formats=['%d-%m-%Y %H:%M:%S', '%Y-%m-%d %H:%M'],
        label='Enter a date/time (e.g., YYYY-MM-DD HH:MM:SS)',
    )

    class Meta:
        model = Stadium
        fields = {
            'name': ['icontains'],
        }

    def filter_datetime_in(self, queryset, name, value):
        """Checks and excludes if value (start or end) is inside of booked time
        """

        queryset = queryset.exclude(
            models.Q(bookings__booked_at__lt=value)\
            &models.Q(bookings__closed_at__gt=value)
        )
        return queryset
