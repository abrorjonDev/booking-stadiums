from django.utils.translation import gettext_lazy as _
from drf_yasg.utils import swagger_auto_schema

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from bookings.models import Booking

from bookings.serializers import BookingListSerializer

from users.models import User


class QuerySetMixin:
    def get_queryset(self):
        filters = {}
        user = self.request.user
        if user.role == User.ROLE.Booking_OWNER:
            filters = {'stadium___created_by': user}
        elif user.role == User.ROLE.USER:
            filters = {'_created_by': user}
        qs = Booking.objects.filter(**filters).select_related('_created_by', '_modified_by', 'stadium')
        return qs


class BookingListCreateAPI(QuerySetMixin, ListCreateAPIView):
    serializer_class = BookingListSerializer
    filterset_fields = {
        'stadium': ['exact'],
        'stadium__name': ['icontains'],
        '_status': ['exact'],
    } 

    @swagger_auto_schema(
        tags=['Bookings.CRUD'], 
        operation_summary="Mainly for `ADMIN` and `Booking OWNER`s")
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Bookings.CRUD'], 
        operation_summary="For Booking by users")
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class BookingRUpdateDeleteAPI(QuerySetMixin, RetrieveUpdateDestroyAPIView):
    serializer_class = BookingListSerializer
    filterset_fields = {
        'stadium': ['exact'],
        'stadium__name': ['icontains'],
        '_status': ['exact'],
    }

    @swagger_auto_schema(
        tags=['Bookings.CRUD'], 
        operation_summary="Mainly for `ADMIN` and `STADIUM OWNER`s")
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Bookings.CRUD'], 
        operation_summary="Mainly for `ADMIN` and `STADIUM OWNER`s")
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Bookings.CRUD'], 
        operation_summary="Mainly for `ADMIN` and `STADIUM OWNER`s")
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Bookings.CRUD'], 
        operation_summary="Mainly for `ADMIN` and `STADIUM OWNER`s, only Users cannot do this action.")
    def delete(self, request, *args, **kwargs):
        if request.user.role == User.ROLE.USER:
            raise Response({"message": "You are not allowed to delete"}, 403)
        return self.destroy(request, *args, **kwargs)
