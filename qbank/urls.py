from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from question import views as q_views
from user import views as u_views

router = DefaultRouter()

router.register(r"departments", q_views.DepartmentAPIViewSet)
router.register(r"courses", q_views.CourseAPIViewSet)
router.register(r"questions", q_views.QuestionAPIViewSet)
router.register(r"users", u_views.UserAPIView)

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r"^api/v1/rest-auth/", include("rest_auth.urls")),
    # path("api/v1/user/<username>/", u_views.UserAPIView.as_view()),
    re_path(r"^api/v1/route/", include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
