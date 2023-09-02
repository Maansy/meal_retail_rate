from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Meal Rate API",
        default_version="v1",
        description="This is a simple API for Meal Rate",
        terms_of_service="https://www.mansy.com/terms/",
        contact=openapi.Contact(email="contact@mansy.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
