from django.urls import path

from stadiums.views import (
    StadiumListAPI, StadiumSearchAPI, StadiumCreateAPI, StadiumRUpdateDeleteAPI,
    ImageListAPIView,
)


app_name = 'stadiums'


urlpatterns = [
    path('stadiums', StadiumListAPI.as_view(), name='stadiums'),
    path('stadiums-search', StadiumSearchAPI.as_view(), name='stadiums-search'),
    path('stadiums/create', StadiumCreateAPI.as_view(), name='stadiums-create'),
    path('stadiums/<int:pk>', StadiumRUpdateDeleteAPI.as_view(), name='stadiums-detail-update-delete'),
    path('images', ImageListAPIView.as_view(), name='image-list'),
]