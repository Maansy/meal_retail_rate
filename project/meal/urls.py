from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('meal', views.MealViewSet, basename='meal')
router.register('rating', views.RatingViewSet, basename='rating')


urlpatterns = [
    path('', include(router.urls)),
]