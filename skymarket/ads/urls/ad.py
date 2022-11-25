from django.urls import path
from rest_framework import routers

from ads.views.ad import (
    AdUploadImageView,
    AdViewSet
)
router = routers.SimpleRouter()
router.register('ad', AdViewSet)


urlpatterns = [
    path('<int:pk>/upload_image/', AdUploadImageView.as_view())
]

urlpatterns += router.urls
