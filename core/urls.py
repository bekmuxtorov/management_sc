from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Management SC",
        default_version="v1",
        description="Management is a study center management system built on Django and Django Rest Framework (DRF). It is an easy management system for educational centers and is my personal startup project.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="asadbekmuxtorov2@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),

    path('swagger/', schema_view.with_ui(
        'swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui(
        'redoc', cache_timeout=0), name='schema-redoc'),

    path('api/', include('account.urls')),
]
