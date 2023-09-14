from drf_yasg.utils import swagger_auto_schema

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView

from stadiums.models import Stadium
from stadiums.filters import StadiumListFilter, StadiumSearchFilter
from stadiums.serializers import StadiumListSerializer, StadiumWriteSerializer

from users.models import User


class QuerySetMixin:
    def get_queryset(self):
        filters = {}
        user = self.request.user
        if user.role == User.ROLE.STADIUM_OWNER:
            filters = {'_created_by': user}
        elif user.role == User.ROLE.USER:
            filters = {'_status': Stadium.STATUS.PUBLISHED}
        qs = Stadium.objects.filter(**filters).select_related('_created_by', '_modified_by').prefetch_related('images')
        return qs


class StadiumListAPI(QuerySetMixin, ListAPIView):
    serializer_class = StadiumListSerializer
    filterset_class = StadiumListFilter

    @swagger_auto_schema(
        tags=['stadiums.CRUD'], 
        operation_summary="Mainly for `ADMIN` and `STADIUM OWNER`s")
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class StadiumSearchAPI(ListAPIView):
    serializer_class = StadiumListSerializer
    filterset_class = StadiumSearchFilter

    def get_queryset(self):
        return Stadium.objects.published()

    @swagger_auto_schema(
        tags=['stadiums.SEARCH'], 
        operation_summary="Used for filtering bookable stadiums")
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class StadiumCreateAPI(QuerySetMixin, CreateAPIView):
    serializer_class = StadiumWriteSerializer

    @swagger_auto_schema(
        tags=['stadiums.CRUD'], 
        operation_summary="Mainly for `ADMIN` and `STADIUM OWNER`s")
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class StadiumRUpdateDeleteAPI(QuerySetMixin, RetrieveUpdateDestroyAPIView):
    serializer_class = StadiumWriteSerializer

    @swagger_auto_schema(
        tags=['stadiums.CRUD'], 
        operation_summary="Mainly for `ADMIN` and `STADIUM OWNER`s")
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['stadiums.CRUD'], 
        operation_summary="Mainly for `ADMIN` and `STADIUM OWNER`s")
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['stadiums.CRUD'], 
        operation_summary="Mainly for `ADMIN` and `STADIUM OWNER`s")
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['stadiums.CRUD'], 
        operation_summary="Mainly for `ADMIN` and `STADIUM OWNER`s")
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
