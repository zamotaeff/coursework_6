from django.urls import include, path

from djoser.views import UserViewSet
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register('user', UserViewSet)


urlpatterns = [
    path('user/auth/', include('djoser.urls'), name="user-auth"),
    path('user/auth/', include('djoser.urls.jwt'), name="user-auth-jwt"),
]

urlpatterns += router.urls

