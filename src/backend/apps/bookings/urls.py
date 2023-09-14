from django.urls import path

from bookings.views import (
    BookingListCreateAPI,
)


app_name = 'bookings'


urlpatterns = [
    path('bookings', BookingListCreateAPI.as_view(), name='bookings-list'),
]

