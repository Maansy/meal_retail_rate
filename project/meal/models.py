from django.db import models

# Create your models here.


class MealRate(models.Model):
    meal = models.CharField(max_length=100)
    rate = models.IntegerField()

    def __str__(self):
        return f'{self.meal} - {self.rate}'
    class Meta:
        db_table = 'meal_rate'
        verbose_name = 'Meal Rate'
        verbose_name_plural = 'Meal Rates'