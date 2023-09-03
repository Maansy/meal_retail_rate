from django.contrib import admin
from django.urls import path, include, re_path
from meal import views
from rest_framework.routers import DefaultRouter
from meal.swagger import schema_view
from rest_framework.authtoken.views import obtain_auth_token
# router = DefaultRouter()
# router.register('meal', views.MealRateViewSet, basename='meal')
# router.register('rating', views.RatingViewSet, basename='rating')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger<str:format>', schema_view.without_ui(
        cache_timeout=0), name='schema-json'),
    path('docs/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
    path('api/', include('meal.urls')),
    path('api-auth/', obtain_auth_token, name='api_token_auth'),
]
