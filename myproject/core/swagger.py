from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


# Configuration for Swagger UI
schema_view = get_schema_view(
    openapi.Info(
        title="API documentation",
        default_version='v1',
        description="",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
