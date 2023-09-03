from django.shortcuts import render
from rest_framework import viewsets, status
from .serializers import MealSerializer, RatingSerializer
from .models import Meal, Rating
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
# Create your views here.

#viewset

class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

    @action(methods=['POST'], detail=True)
    #http://127.0.0.1:8000/api/meal/1/rate_meal/ > 1 = meal id and pk
    def rate_meal(self,request, pk=None):
        if 'stars' in request.data:
            if 'username' in request.data:
                meal = Meal.objects.get(id=pk) 
                username = request.data['username'] 
                stars = request.data['stars']
                user = User.objects.get(username=username)
                try:
                    #update rating
                    rate = Rating.objects.get(user=user.id, meal=meal.id)
                    rate.stars = stars
                    rate.save()
                    serailzer = RatingSerializer(rate, many=False)
                    response = {'message': 'rating updated', 'result': serailzer.data}
                    return Response(response,status=status.HTTP_200_OK)
                except:
                    #create rating
                    rate = Rating.objects.create(user=user, meal=meal, stars=stars)
                    serailzer = RatingSerializer(rate, many=False)
                    response = {'message': 'rating created', 'result': serailzer.data}
                    return Response(response,status=status.HTTP_200_OK)
            else:
                response = {'message': 'you need to provide username'}
                return Response(response,status=status.HTTP_400_BAD_REQUEST)
        else:
            response = {'message': 'you need to provide stars'}
            return Response(response,status=status.HTTP_400_BAD_REQUEST)

    #retun no of users ,rating , and meals
    @action(methods=['GET'], detail=False)
    def resturant_statistic(self,request):
        no_meals = Meal.objects.all()
        no_ratings = Rating.objects.all()
        no_users = User.objects.all()
        return Response({"number of meals in our database is": len(no_meals),
                         "number of users is": len(no_users),
                         "number of ratings is": len(no_ratings)},
                         status=status.HTTP_200_OK)

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer