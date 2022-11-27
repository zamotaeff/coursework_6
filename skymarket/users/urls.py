from django.urls import include, path, re_path

from djoser.views import UserViewSet
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = SimpleRouter()
router.register('users', UserViewSet, basename="users")


urlpatterns = [
    path("", include(router.urls)),
    re_path(r'^auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.jwt')),

    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]
