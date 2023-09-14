from drf_yasg.utils import swagger_auto_schema

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.parsers import MultiPartParser

from stadiums.models import StadiumImage, Stadium
from stadiums.serializers import ImageSerializer

from users.models import User


class ImageListAPIView(ListCreateAPIView):
    serializer_class = ImageSerializer
    queryset = StadiumImage.objects.all().select_related('stadium')
    filterset_fields = ('stadium',)
    parser_classes = (MultiPartParser,)

    @swagger_auto_schema(
        tags=['stadiums.CRUD'], 
        operation_summary="Mainly for `ADMIN` and `STADIUM OWNER`s to upload images")
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['stadiums.CRUD'], 
        operation_summary="Mainly for `ADMIN` and `STADIUM OWNER`s to upload images")
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)