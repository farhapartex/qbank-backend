from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r"^api/v1/rest-auth/", include("rest_auth.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
