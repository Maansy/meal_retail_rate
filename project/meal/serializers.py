from rest_framework.serializers import ModelSerializer

from .models import MealRate

class MealRateSerializer(ModelSerializer):
    class Meta:
        model = MealRate
        fields = '__all__'