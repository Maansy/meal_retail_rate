from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.



class Meal(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Meal'
        verbose_name_plural = 'Meals'

class Rating(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return self.meal.title + ' - ' + self.user.username
    
    class Meta:
        verbose_name = 'Rating'
        verbose_name_plural = 'Ratings'
        unique_together = (('user', 'meal'),)
        index_together = (('user', 'meal'),)

