from django.contrib import admin

from bookings.models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('stadium', 'status', 'cost', 'booked_at', 'closed_at')
    list_filter = ('_status', 'stadium')
    date_hierarchy = 'booked_at'

    search_fields = ('stadium__name',)
    search_help_text = "Search by entering `stadium name`"

    list_per_page = 25
