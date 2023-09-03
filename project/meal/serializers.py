from rest_framework.serializers import ModelSerializer

from .models import Meal, Rating
from django.contrib.auth.models import User

# why we use serializers?
# serializers are used to convert complex data like querysets and model instances to native python datatypes
# that can then be easily rendered into json, xml or other content types.
# serializers also provide deserialization, allowing parsed data to be converted back into complex types,
# after first validating the incoming data.
class MealSerializer(ModelSerializer):
    class Meta:
        model = Meal
        fields = ('id', 'title', 'description','no_of_ratings','avg_rating')

class RatingSerializer(ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'stars', 'user', 'meal')

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password':{'write_only':True, 'required':True}}

