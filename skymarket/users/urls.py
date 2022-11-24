from django.urls import include, path
from djoser.views import UserViewSet
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register('user', UserViewSet)


urlpatterns = [
]

urlpatterns += router.urls

