from django.shortcuts import render
from rest_framework import viewsets, status
from .serializers import MealSerializer, RatingSerializer, UserSerializer
from .models import Meal, Rating
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.authtoken.models import Token
# Create your views here.

#viewset

class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @action(methods=['POST'], detail=True)
    #http://127.0.0.1:8000/api/meal/1/rate_meal/ > 1 = meal id and pk
    def rate_meal(self,request, pk=None):
        if 'stars' in request.data:
            meal = Meal.objects.get(id=pk) 
            stars = request.data['stars']
            user = request.user
            # print('user',user)
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

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        response = {'message': 'you cant update rating like that'}
        return Response(response,status=status.HTTP_400_BAD_REQUEST)
    
    def create(self, request, *args, **kwargs):
        response = {'message': 'you cant create rating like that'}
        return Response(response,status=status.HTTP_400_BAD_REQUEST)
    

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]

    # def update(self, request, *args, **kwargs):
    #     response = {'message': 'you cant update user like that'}
    #     return Response(response,status=status.HTTP_400_BAD_REQUEST)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True) #if serializer is not valid raise exception
        self.perform_create(serializer)
        token, created = Token.objects.get_or_create(user=serializer.instance)
        return Response({'token': token.key}, status=status.HTTP_201_CREATED)
    
    def list(self, request, *args, **kwargs):
        response = {'message': 'you cant list users like that'}
        return Response(response,status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, *args, **kwargs):
        response = {'message': 'you cant retrieve users like that'}
        return Response(response,status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, *args, **kwargs):
        response = {'message': 'you cant destroy users like that'}
        return Response(response,status=status.HTTP_400_BAD_REQUEST)
        