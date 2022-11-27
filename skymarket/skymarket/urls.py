from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    path("api/admin/", admin.site.urls),

    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),

    path("api/schema/redoc-tasks/", include("redoc.urls")),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    path('api/', include('users.urls')),
    path('api/', include('ads.urls.ad')),
    path('api/', include('ads.urls.comment'))
]

# To display images when debugging mode
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
